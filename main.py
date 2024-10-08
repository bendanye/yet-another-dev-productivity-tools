from streamlit_navigation_bar import st_navbar

import streamlit as st
import pages as pg

st.set_page_config(initial_sidebar_state="collapsed")

OPTIONS = {"show_menu": False, "show_sidebar": False, "hide_nav": True}

STYLES = {
    "nav": {
        "background-color": "royalblue",
        "justify-content": "left",
    },
    "div": {
        "max-width": "90rem",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    },
}

page = st_navbar(
    [
        "Home",
        "String Transformation",
        "Template",
        "Duplicate",
        "List conversion",
        "Compare Lists",
        "Vlookup",
        "Copy Json inside json",
        "Compare Yaml Keys",
        "URL Query Params",
    ],
    styles=STYLES,
    options=OPTIONS,
)

functions = {
    "Home": pg.show_home,
    "String Transformation": pg.show_transformation,
    "Template": pg.show_template,
    "Duplicate": pg.show_duplicate,
    "List conversion": pg.show_list_conversion,
    "Compare Lists": pg.show_compare_lists,
    "Vlookup": pg.show_vlookup,
    "Copy Json inside json": pg.show_copy_json,
    "Compare Yaml Keys": pg.show_yaml_key_comparator,
    "URL Query Params": pg.show_url_query_params,
}

if "page" in st.query_params:
    page = st.query_params["page"]

go_to = functions.get(page)
if go_to:
    go_to()
