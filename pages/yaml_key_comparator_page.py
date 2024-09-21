import streamlit as st
import yaml

from pages.yaml_key_comparator import compare_yaml_by_content


def show_yaml_key_comparator():
    st.title("Yaml Key Comparator")
    st.write("This tool is to compare two yaml keys")

    fields_columns = st.columns([3, 3])
    with fields_columns[0]:
        standard = st.text_area("Yaml (Standard)", key="standard_input", height=400)
    with fields_columns[1]:
        to_compare = st.text_area(
            "Yaml (To compare)", key="to_compare_input", height=400
        )

    if standard and to_compare:
        missing_from_source, extra_from_to_compare = compare_yaml_by_content(
            standard, to_compare
        )
        if not missing_from_source and not extra_from_to_compare:
            st.write("No differences!")
        else:
            st.write("Missing from Source")
            st.write("============")
            st.write(missing_from_source)
            st.write("============")

            st.write("Extra in To compare")
            st.write("============")
            st.write(extra_from_to_compare)
            st.write("============")


if __name__ == "__main__":
    show_yaml_key_comparator()
