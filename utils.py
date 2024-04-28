import requests
from lxml import html
from typing import Optional


def get_html(url: str) -> Optional[str]:

    response = requests.get(url)
    response.encoding = response.apparent_encoding
    if response.status_code == 200:
        return response.text
    return None


def parse_field(res_str: str, parse_reg: str) -> list:

    parse_obj = html.fromstring(res_str)
    parse_res = parse_obj.xpath(parse_reg)

    if not parse_res:
        return []
    return parse_res


def parse_field_from_node_obj(node_obj: str, parse_reg: str) -> list:

    parse_res = node_obj.xpath(parse_reg)

    if not parse_res:
        return []
    return parse_res

