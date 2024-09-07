import streamlit as st
import json


def show_copy_json():
    st.title("Copy Json inside json")
    st.write("This tool is to get json in a json")

    key = st.text_input("key contains json")
    enter_json = st.text_area("Paste the whole json values", height=200)

    if key and enter_json:
        if key not in enter_json:
            st.write(f"{key} not found in the given json")
        else:
            json_obj = json.loads(enter_json)
            selected_json = json_obj[key]

            st.write("Output")
            st.json(selected_json, expanded=2)


if __name__ == "__main__":
    show_copy_json()
