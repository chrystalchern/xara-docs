from docutils import nodes
from sphinx import addnodes

try:
    from sphinx.domains.python._object import PyObject, PyTypedField
except ImportError:
    from sphinx.domains.python import PyObject, PyTypedField


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


def patch_python_parameters():
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

    if hasattr(PyObject, "_doc_field_type_map"):
        PyObject._doc_field_type_map = {}


def setup(app):
    patch_python_parameters()

    return {
        "version": "0.3",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }