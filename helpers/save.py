from html import escape
from jinja2 import Template, Environment, meta


def get_to_save(string: str):
    string = escape(string)
    env = Environment()
    ast = env.parse(string)
    vars = meta.find_undeclared_variables(ast)

    if 'end_c' not in vars:
        return string

    kwargs = {}

    for var in vars:
        if var.startswith('c_'):
            kwargs[var] = f'<span style="color: #{var[2:]};">'
        elif var == ('end_c'):
            kwargs[var] = '</span>'
        else:
            kwargs[var] = '{{' + var + '}}'

    if 'c_' in kwargs:
        return string

    return Template(string).render(kwargs)
