"""version_notes.py

A small Sphinx extension that provides version-tagged notes which also
aggregate onto a single changelog page.

It defines two directives, modelled on Sphinx's own ``todo`` / ``todolist``
pair:

    .. version-note::
       :version: 1.2
       :type: changed          # optional: added | changed | deprecated | removed | fixed

       A change was introduced to this function ...

    .. version-changelog::

``version-note`` renders an admonition inline at its original location and
records the entry on the build environment. ``version-changelog`` is replaced
at resolve time by every recorded entry, grouped by version (newest first),
each carrying a breadcrumb back to its source location.

For lighter-weight, inline annotations (for instance, marking a newly added
function parameter) it also provides a family of roles:

    The ``timeout`` parameter :version-added:`0.1.28` controls ...

    Pass a description for a richer changelog entry:
    :version-added:`the timeout parameter <0.1.28>`

Available roles: ``version-added``, ``version-changed``, ``version-deprecated``,
``version-removed`` and ``version-fixed``. Each renders a small inline marker
and, unless ``version_notes_inline_in_changelog`` is set to ``False`` in
``conf.py``, feeds the same changelog as the block directive.
"""

from __future__ import annotations

import re

from docutils import nodes
from docutils.parsers.rst import directives

from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective, SphinxRole

#
# Version parsing / sorting
#

_OPERATOR_RE = re.compile(r"^\s*(?:>=|<=|==|~=|!=|>|<)?\s*(.+?)\s*$")


def _strip_operator(raw: str) -> str:
    """Drop a leading comparison operator, leaving the bare version string."""
    match = _OPERATOR_RE.match(raw)
    return match.group(1) if match else raw


try:  # robust ordering when packaging is installed (it usually is)
    from packaging.version import InvalidVersion, Version

    def _version_key(raw: str):
        try:
            return (0, Version(_strip_operator(raw)))
        except InvalidVersion:
            return (1, _strip_operator(raw))  # unparseable: sort last, lexically
except ModuleNotFoundError:  # naive fallback

    def _version_key(raw: str):
        cleaned = _strip_operator(raw)
        parts = re.split(r"[.\-]", cleaned)
        numeric = tuple(int(p) if p.isdigit() else -1 for p in parts)
        return (0, numeric, cleaned)


#
# Custom nodes
#


class version_note(nodes.Admonition, nodes.Element):
    """Rendered inline as an admonition; also recorded for the changelog."""


class version_changelog(nodes.General, nodes.Element):
    """Placeholder, replaced by the aggregated changelog at resolve time."""


def visit_version_note(self, node):
    self.visit_admonition(node)


def depart_version_note(self, node):
    self.depart_admonition(node)


#
# Directives
#

_TYPES = ("added", "changed", "deprecated", "removed", "fixed")


def _type_option(value: str) -> str:
    value = (value or "").strip().lower()
    if value and value not in _TYPES:
        raise ValueError(
            "version-note :type: must be one of "
            f"{', '.join(_TYPES)}; got {value!r}"
        )
    return value


class VersionNoteDirective(SphinxDirective):
    has_content = True
    option_spec = {
        "version": directives.unchanged_required,
        "type": _type_option,
    }

    def run(self):
        version = self.options["version"].strip().strip("\"'")
        change_type = self.options.get("type", "")

        admonition = version_note("\n".join(self.content))
        if change_type:
            title_text = f"{change_type.capitalize()} in {version}"
        else:
            title_text = f"Version {version}"
        admonition += nodes.title(text=title_text)
        self.state.nested_parse(self.content, self.content_offset, admonition)

        # An anchor so the changelog can link back to this spot.
        target_id = f"version-note-{self.env.new_serialno('version-note')}"
        target = nodes.target("", "", ids=[target_id])

        # The body is everything except the synthesised title.
        body = [
            child.deepcopy()
            for child in admonition.children
            if not isinstance(child, nodes.title)
        ]
        _record_entry(self.env, self.env.docname, self.lineno,
                      version, change_type, target_id, body)

        return [target, admonition]


class VersionChangelogDirective(SphinxDirective):
    has_content = False

    def run(self):
        if not hasattr(self.env, "version_changelog_docs"):
            self.env.version_changelog_docs = set()
        self.env.version_changelog_docs.add(self.env.docname)
        return [version_changelog("")]


#
# Shared recorder + inline roles
#


def _record_entry(env, docname, lineno, version, change_type, target_id, body):
    """Append one entry to the changelog store on the build environment."""
    if not hasattr(env, "version_notes_all"):
        env.version_notes_all = []
    env.version_notes_all.append(
        {
            "docname": docname,
            "lineno": lineno,
            "version": version,
            "type": change_type,
            "target_id": target_id,
            "body": body,
        }
    )


# Inline label for each marker type. The block directive uses the same wording.
_INLINE_LABELS = {
    "added": "Added in {}",
    "changed": "Changed in {}",
    "deprecated": "Deprecated since {}",
    "removed": "Removed in {}",
    "fixed": "Fixed in {}",
}

# ``description <version>`` form, mirroring Sphinx's own explicit-title roles.
_EXPLICIT_RE = re.compile(r"^(.+?)\s*<(.+?)>$", re.DOTALL)


class VersionMarkerRole(SphinxRole):
    """Inline counterpart to ``version-note``. ``change_type`` is bound per role
    by :func:`_make_marker_role`."""

    change_type = "added"

    def run(self):
        match = _EXPLICIT_RE.match(self.text.strip())
        if match:
            description, version = match.group(1).strip(), match.group(2).strip()
        else:
            description, version = "", self.text.strip()
        version = version.strip("\"'")

        label = _INLINE_LABELS[self.change_type].format(version)
        target_id = f"version-note-{self.env.new_serialno('version-note')}"
        marker = nodes.inline(
            self.rawtext,
            label,
            classes=["versionmod", f"version-{self.change_type}"],
            ids=[target_id],
        )

        if self.config.version_notes_inline_in_changelog:
            body = [nodes.paragraph("", "", nodes.Text(description))] if description else []
            _record_entry(self.env, self.env.docname, self.lineno,
                          version, self.change_type, target_id, body)

        return [marker], []


def _make_marker_role(change_type):
    return type(
        f"VersionMarkerRole_{change_type}",
        (VersionMarkerRole,),
        {"change_type": change_type},
    )

#
# Build-environment bookkeeping
#

def purge_version_notes(app, env, docname):
    """Drop entries from a document before it is re-read."""
    if hasattr(env, "version_notes_all"):
        env.version_notes_all = [
            e for e in env.version_notes_all if e["docname"] != docname
        ]
    if hasattr(env, "version_changelog_docs"):
        env.version_changelog_docs.discard(docname)


def merge_version_notes(app, env, docnames, other):
    """Merge state collected in parallel-build subprocesses."""
    if not hasattr(env, "version_notes_all"):
        env.version_notes_all = []
    if hasattr(other, "version_notes_all"):
        env.version_notes_all.extend(other.version_notes_all)

    if not hasattr(env, "version_changelog_docs"):
        env.version_changelog_docs = set()
    if hasattr(other, "version_changelog_docs"):
        env.version_changelog_docs |= other.version_changelog_docs


def _is_marker(node):
    return isinstance(node, nodes.inline) and "versionmod" in node.get("classes", [])


def _enclosing_param(marker, parent_map):
    """Return the name of the parameter a marker annotates, or ``None``.

    This walks outward from the marker and stops at the first container it
    recognises, so that when several parameters are listed together the nearest
    one wins rather than the first in the list. It understands two renderings:

    * stock Sphinx, where the parameter name is a ``literal_strong`` inside the
      marker's own list item (multiple parameters) or field body (a single one);
    * a definition-list rendering, where the name is a ``literal_strong`` in the
      ``term`` of the enclosing ``definition_list_item``.

    The name node may be wrapped in a ``pending_xref`` at this stage, which
    ``findall`` sees through."""
    node = marker
    while id(node) in parent_map:
        node = parent_map[id(node)]

        if isinstance(node, nodes.definition_list_item):
            term = next(
                (child for child in node.children if isinstance(child, nodes.term)),
                None,
            )
            scope = term if term is not None else node
            found = next(scope.findall(addnodes.literal_strong), None)
            return found.astext() if found is not None else None

        if isinstance(node, (nodes.list_item, nodes.field_body)):
            found = next(node.findall(addnodes.literal_strong), None)
            return found.astext() if found is not None else None

    return None


def annotate_param_context(app, env):
    """Tag each marker's changelog entry with the parameter it annotates, if any.

    Sphinx only renders an info-field ``:param:`` into its final form (where the
    parameter name is a ``literal_strong`` node) after the per-document read
    handlers have run, so the structure is not visible at ``doctree-read``. We
    therefore read each stored doctree back here, once the whole read phase is
    complete, and recompute from scratch so incremental builds stay correct."""
    entries = getattr(env, "version_notes_all", None)
    if not entries:
        return []

    by_doc: dict[str, dict] = {}
    for entry in entries:
        entry.pop("param", None)  # recompute cleanly on every build
        by_doc.setdefault(entry["docname"], {})[entry["target_id"]] = entry

    for docname, id_map in by_doc.items():
        try:
            doctree = env.get_doctree(docname)
        except Exception:
            continue

        parent_map = {}
        for node in doctree.findall():
            for child in node.children:
                parent_map[id(child)] = node

        for marker in doctree.findall(_is_marker):
            for marker_id in marker.get("ids", []):
                entry = id_map.get(marker_id)
                if entry is not None:
                    name = _enclosing_param(marker, parent_map)
                    if name:
                        entry["param"] = name
                    break

    # Force any page holding a changelog to be rewritten, so the aggregation
    # reflects notes that changed on other pages during an incremental build.
    return sorted(getattr(env, "version_changelog_docs", set()))


#
# Assemble the changelog at resolve time
#


_CRUMB_SEP = "\u00a0\u203a\u00a0"  # non-breaking space, single right angle quote


def _page_chain(docname, relations):
    """Docnames from the root toctree page down to ``docname``."""
    chain, seen = [], set()
    while docname is not None and docname not in seen:
        seen.add(docname)
        chain.append(docname)
        docname = relations.get(docname, [None])[0]
    chain.reverse()
    return chain


def _crumb_ref(app, fromdocname, target_docname, anchor, content):
    ref = nodes.reference("", "")
    ref["refdocname"] = target_docname
    uri = app.builder.get_relative_uri(fromdocname, target_docname)
    if anchor:
        uri += "#" + anchor
    ref["refuri"] = uri
    ref += content
    return ref


def _breadcrumb(app, fromdocname, entry, relations):
    """A breadcrumb to the source of the change. Page crumbs link to their
    pages; the final crumb (the parameter name when present, otherwise the page)
    links to the annotated spot itself."""
    env = app.builder.env
    chain = _page_chain(entry["docname"], relations)
    param = entry.get("param")

    crumbs = []
    for index, docname in enumerate(chain):
        title_node = env.titles.get(docname)
        label = title_node.astext() if title_node is not None else docname
        on_page = index == len(chain) - 1
        anchor = entry["target_id"] if (on_page and not param) else None
        crumbs.append(_crumb_ref(app, fromdocname, docname, anchor, nodes.Text(label)))

    if param:
        crumbs.append(
            _crumb_ref(
                app, fromdocname, entry["docname"], entry["target_id"],
                nodes.literal("", param),
            )
        )

    para = nodes.paragraph(classes=["version-note-breadcrumb"])
    for index, crumb in enumerate(crumbs):
        para += crumb
        if index != len(crumbs) - 1:
            para += nodes.Text(_CRUMB_SEP)
    return para


def process_changelog_nodes(app, doctree, fromdocname):
    env = app.builder.env
    entries = list(getattr(env, "version_notes_all", []))
    relations = env.collect_relations()

    for changelog_node in list(doctree.findall(version_changelog)):
        if not entries:
            changelog_node.replace_self([])
            continue

        grouped: dict[str, list] = {}
        for entry in entries:
            grouped.setdefault(entry["version"], []).append(entry)

        container = nodes.container(classes=["version-changelog"])
        for version in sorted(grouped, key=_version_key, reverse=True):
            container += nodes.rubric(text=f"Version {version}")

            bullets = nodes.bullet_list()
            for entry in grouped[version]:
                item = nodes.list_item()

                body = [child.deepcopy() for child in entry["body"]]
                if entry["type"] and body and isinstance(body[0], nodes.paragraph):
                    body[0].insert(
                        0, nodes.strong(text=f"{entry['type'].capitalize()}: ")
                    )
                elif not body:
                    # An inline marker with no description: show the type label,
                    # and let the breadcrumb point at the exact annotated spot.
                    caption = entry["type"].capitalize() if entry["type"] else "Note"
                    body = [nodes.paragraph("", "", nodes.strong(text=caption))]
                for child in body:
                    item += child

                item += _breadcrumb(app, fromdocname, entry, relations)
                bullets += item

            container += bullets

        changelog_node.replace_self(container)


#
# Registration
#


def setup(app: Sphinx):
    app.add_node(version_changelog)
    app.add_node(
        version_note,
        html=(visit_version_note, depart_version_note),
        latex=(visit_version_note, depart_version_note),
        text=(visit_version_note, depart_version_note),
        man=(visit_version_note, depart_version_note),
        texinfo=(visit_version_note, depart_version_note),
    )

    app.add_directive("version-note", VersionNoteDirective)
    app.add_directive("version-changelog", VersionChangelogDirective)

    for change_type in _INLINE_LABELS:
        app.add_role(f"version-{change_type}", _make_marker_role(change_type)())

    app.add_config_value("version_notes_inline_in_changelog", True, "env")

    app.connect("env-purge-doc", purge_version_notes)
    app.connect("env-merge-info", merge_version_notes)
    app.connect("env-updated", annotate_param_context)
    app.connect("doctree-resolved", process_changelog_nodes)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }