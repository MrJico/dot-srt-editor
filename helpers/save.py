import re
from html import escape


def get_to_save(string: str):
    match_list = re.findall(
        r"(<#([aA-zZ]+|[aA-fF0-9]{6})#(\s*[\w\s]+\s*)>)", string, flags=re.UNICODE
    )
    if match_list:
        for match in match_list:
            color = match[1]
            text = escape(match[2].strip())
            colored = f'<span style="color: #{color};">{text}</span>'
            string = string.replace(match[0], colored)

        return string

    return string.strip()
