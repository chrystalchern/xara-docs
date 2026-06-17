# docs/_ext/grouped_params.py

import hashlib
import re
import shlex

from docutils import nodes
from sphinx import addnodes

try:
    from sphinx.domains.python._object import PyObject, PyTypedField
except ImportError:
    from sphinx.domains.python import PyObject, PyTypedField


_DYNAMIC_FIELD_NAMES = set()


def _first_source_line(*objects):
    for obj in objects:
        if obj is None:
            continue

        if isinstance(obj, (list, tuple)):
            found = _first_source_line(*obj)
            if found is not None:
                return found
            continue

        source = getattr(obj, "source", None)
        line = getattr(obj, "line", None)

        if source is not None or line is not None:
            if not isinstance(line, int):
                line = 1
            return source or "", line

    return "", 1


def _stamp(node, source, line):
    node.source = source
    node.line = line
    if not getattr(node, "rawsource", None):
        node.rawsource = node.astext()
    return node


# def _split_field_name(text):
#     try:
#         return text.split(None, 1)
#     except ValueError:
#         return text, ""
def _split_field_name(text):
    parts = text.split(None, 1)

    if len(parts) == 0:
        return "", ""

    if len(parts) == 1:
        return parts[0], ""

    return parts[0], parts[1]


# def _parse_gparam_arg(arg):
#     parts = shlex.split(arg)

#     if len(parts) == 1:
#         return "Parameters", parts[0]

#     if len(parts) >= 2:
#         return " ".join(parts[:-1]), parts[-1]

#     return "Parameters", ""

# def _parse_gparam_arg(arg):
#     parts = shlex.split(arg)

#     if len(parts) == 1:
#         return "Parameters", parts[0]

#     if len(parts) >= 2:
#         return " ".join(parts[:-1]), parts[-1]

#     return "Parameters", ""
def _parse_gparam_arg(arg):
    try:
        parts = shlex.split(arg)
    except ValueError:
        return "Parameters", ""

    if len(parts) == 1:
        return "Parameters", parts[0]

    if len(parts) >= 2:
        return " ".join(parts[:-1]), parts[-1]

    return "Parameters", ""


def _slug(label):
    base = re.sub(r"[^a-zA-Z0-9]+", "_", label).strip("_").lower()
    digest = hashlib.sha1(label.encode("utf-8")).hexdigest()[:8]

    if not base:
        base = "group"

    return f"{base}_{digest}"


def _set_field_name(field_name, text):
    field_name.clear()
    field_name += nodes.Text(text)


class DLParameterField(PyTypedField):
    def make_field(
        self,
        types,
        domain,
        items,
        env=None,
        inliner=None,
        location=None,
    ):
        source, line = _first_source_line(location, [content for _, content in items])

        field_name = nodes.field_name()
        field_name += nodes.Text(self.label)

        dl = nodes.definition_list(classes=["py-parameter-list"])

        for fieldarg, content in items:
            item = nodes.definition_list_item()
            term = nodes.term()

            term.extend(
                self.make_xrefs(
                    self.rolename,
                    domain,
                    fieldarg,
                    addnodes.literal_strong,
                    env=env,
                    inliner=inliner,
                    location=location,
                )
            )

            fieldtype = types.pop(fieldarg, None)
            if fieldtype:
                term += nodes.Text(" ")
                type_span = nodes.inline(classes=["param-type"])
                type_span += nodes.Text("(")

                if len(fieldtype) == 1 and isinstance(fieldtype[0], nodes.Text):
                    type_span.extend(
                        self.make_xrefs(
                            self.typerolename,
                            domain,
                            fieldtype[0].astext(),
                            addnodes.literal_emphasis,
                            env=env,
                            inliner=inliner,
                            location=location,
                        )
                    )
                else:
                    type_span.extend(fieldtype)

                type_span += nodes.Text(")")
                term += type_span

            definition = nodes.definition()
            if content:
                paragraph = nodes.paragraph()
                paragraph.extend(content)
                definition += paragraph

            item += term
            item += definition
            dl += item

            _stamp(term, source, line)
            _stamp(definition, source, line)
            _stamp(item, source, line)

        body = nodes.field_body()
        body += dl

        field = nodes.field()
        field += field_name
        field += body

        for node in (field_name, dl, body, field):
            _stamp(node, source, line)

        return field


def _make_param_field(name, label, names, typenames):
    return DLParameterField(
        name,
        label=label,
        names=tuple(names),
        typenames=tuple(typenames),
        rolename="obj",
        typerolename="class",
        can_collapse=False,
    )


def _clear_field_type_cache():
    if hasattr(PyObject, "_doc_field_type_map"):
        PyObject._doc_field_type_map = {}


def _replace_builtin_param_field():
    new_fields = []

    for field in PyObject.doc_field_types:
        if getattr(field, "name", None) == "parameter":
            new_fields.append(
                DLParameterField(
                    "parameter",
                    label=field.label,
                    names=field.names,
                    typenames=field.typenames,
                    rolename=field.rolename,
                    typerolename=field.typerolename,
                    can_collapse=False,
                )
            )
        else:
            new_fields.append(field)

    PyObject.doc_field_types = new_fields
    _clear_field_type_cache()


# def _ensure_dynamic_group(label):
#     slug = _slug(label)
#     field_name = f"gparam_{slug}"

#     if field_name in _DYNAMIC_FIELD_NAMES:
#         return slug

#     PyObject.doc_field_types.append(
#         _make_param_field(
#             name=field_name,
#             label=label,
#             names=(field_name,),
#             typenames=(f"gtype_{slug}",),
#         )
#     )

#     _DYNAMIC_FIELD_NAMES.add(field_name)
#     _clear_field_type_cache()

#     return slug
def _ensure_dynamic_group(label):
    if label in {"Parameter", "Parameters"}:
        slug = "default"
        field_name = "gparam_default"
        field_label = "Parameters"
    else:
        slug = _slug(label)
        field_name = f"gparam_{slug}"
        field_label = label

    if field_name in _DYNAMIC_FIELD_NAMES:
        return slug

    PyObject.doc_field_types.append(
        _make_param_field(
            name=field_name,
            label=field_label,
            names=(field_name,),
            typenames=(f"gtype_{slug}",),
        )
    )

    _DYNAMIC_FIELD_NAMES.add(field_name)
    _clear_field_type_cache()

    return slug

def _rewrite_grouped_param_fields(app, domain, objtype, contentnode):
    if domain != "py":
        return

    for child in list(contentnode):
        if not isinstance(child, nodes.field_list):
            continue

        param_to_slug = {}
        field_rewrites = []

        for field in list(child):
            if len(field) != 2:
                continue

            field_name = field[0]
            kind, arg = _split_field_name(field_name.astext())

            if kind != "gparam":
                continue

            label, param = _parse_gparam_arg(arg)
            if not param:
                continue

            slug = _ensure_dynamic_group(label)
            param_to_slug[param] = slug
            field_rewrites.append((field_name, f"gparam_{slug} {param}"))

        for field_name, new_name in field_rewrites:
            _set_field_name(field_name, new_name)

        for field in list(child):
            if len(field) != 2:
                continue

            field_name = field[0]
            kind, arg = _split_field_name(field_name.astext())

            if kind != "gtype":
                continue

            param = arg.strip()
            slug = param_to_slug.get(param)

            if slug is not None:
                _set_field_name(field_name, f"gtype_{slug} {param}")


def setup(app):
    _replace_builtin_param_field()

    app.connect("object-description-transform", _rewrite_grouped_param_fields)

    return {
        "version": "0.4",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
