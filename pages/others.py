import streamlit as st
import pages as pg


def show_others():
    st.title("Others")

    st.write(f"This is list of less commonly used tools that you may find it useful.")

    st.page_link("pages/copy_json_inside_json.py")
    st.page_link("pages/yaml_key_comparator_page.py")
    st.page_link("pages/url_query_params.py")
    st.page_link("pages/command_polling.py")


if __name__ == "__main__":
    show_others()
