from streamlit_navigation_bar import st_navbar

import streamlit as st
import pages as pg

OPTIONS = {"show_menu": False, "show_sidebar": False, "hide_nav": True}

page = st_navbar(
    [
        "Home",
        "String Transformation",
        "Template",
        "List conversion",
        "Copy Json inside json",
    ],
    options=OPTIONS,
)

functions = {
    "Home": pg.show_home,
    "String Transformation": pg.show_transformation,
    "Template": pg.show_template,
    "List conversion": pg.show_list_conversion,
    "Copy Json inside json": pg.show_copy_json,
}

if "page" in st.query_params:
    page = st.query_params["page"]

go_to = functions.get(page)
if go_to:
    go_to()
