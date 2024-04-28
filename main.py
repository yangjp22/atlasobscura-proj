import streamlit as st

from utils import get_html, parse_field, parse_field_from_node_obj


st.header("请输入你的链接")
url = st.text_input("请输入你的链接: ", label_visibility="hidden")
if url:
    home_str = get_html(url)

    if not home_str:
        str.write("No content, please check if the url is correct or use another url")

    title_reg = "//header[contains(@class, 'item-header')]//div[contains(@class,'list-title')]/h1/text()"
    title = "".join(parse_field(home_str, title_reg))
    st.write("主标题: ", title)

    sub_title_reg = "//header[contains(@class, 'item-header')]//h2[contains(@class, 'editable-subtitle')]/text()"
    sub_title = "".join(parse_field(home_str, sub_title_reg))
    st.write("副标题: ", sub_title)

    cnt_reg = "//div[@class='item-body']/p"
    content = "\n\n".join([each.xpath("string(.)").strip() for each in parse_field(home_str, cnt_reg)])
    st.write("内容：", content.strip())

    sec_reg = "//section[contains(@class, 'list-places')]//a[contains(@class, 'content-card')]"
    sections = parse_field(home_str, sec_reg)
    if sections:
        for idx, sec in enumerate(sections):
            place_title_reg = "div/h3[contains(@class, 'content-card-title')]/span/text()"
            place_title = "".join(parse_field_from_node_obj(sec, place_title_reg))
            st.write("第{}处景点: ".format(idx + 1), place_title)

            href_reg = "@href"
            href = "https://www.atlasobscura.com" + "".join(parse_field_from_node_obj(sec, href_reg))
            st.write("主页链接: ", href)

            place_loc_reg = "div/div[contains(@class, 'place-card-location')]/text()"
            place_loc = "".join(parse_field_from_node_obj(sec, place_loc_reg))
            st.write("地址: ", place_loc)

            place_html = get_html(href)
            if not place_html:
                st.write("详细内容: 无")

            place_cnt_reg = "//div[@id='place-body']//p"
            place_cnt = "\n\n".join([each.xpath("string(.)").strip() for each in parse_field(place_html, place_cnt_reg)])
            st.write("详细内容：", place_cnt.strip())

            place_cautious_reg = "//div[@class='DDP__direction-copy']/p"
            place_cautious = "\n\n".join([each.xpath("string(.)").strip() for each in parse_field(place_html, place_cautious_reg)])
            st.write("去前须知：", place_cautious.strip())

            st.write("\n\n")
