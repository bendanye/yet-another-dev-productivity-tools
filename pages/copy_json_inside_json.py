import streamlit as st
import json


def show_copy_json():
    st.title("Copy Json inside json")
    st.write("This tool is to get json in a json")

    columns = st.columns([1, 6])
    with columns[0]:
        st.button("Clear", on_click=_clear_inputs)
    with columns[1]:
        st.button("Show Inputs Example", on_click=_show_example)

    key = st.text_input("key contains json", key="key_input")
    enter_json = st.text_area(
        "Paste the whole json values", height=200, key="json_input"
    )

    if key and enter_json:
        if key not in enter_json:
            st.write(f"{key} not found in the given json")
        else:
            json_obj = json.loads(enter_json)
            selected_json = json_obj[key]

            st.write("Output")
            st.json(selected_json, expanded=2)


def _clear_inputs():
    st.session_state.key_input = ""
    st.session_state.json_input = ""


def _show_example():
    st.session_state.key_input = "value"
    st.session_state.json_input = """{
    "success": true,
    "value": "{\\"hello\\": \\"testing\\"}"
}"""


if __name__ == "__main__":
    show_copy_json()
