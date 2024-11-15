import streamlit as st

from pages.splitter import split


def show_combined():
    st.title("Combined")
    st.write(
        "This tool is to convert both set of data from each row into combined a single row"
    )

    columns = st.columns([1, 6])
    with columns[0]:
        st.button("Clear", on_click=_clear_inputs)
    with columns[1]:
        st.button("Show Inputs Example", on_click=_show_example)

    fields_columns = st.columns([3, 3, 3, 3])
    with fields_columns[0]:
        ds1_input = st.text_area("Data Set 1", height=400, key="ds1_input")
    with fields_columns[1]:
        ds2_input = st.text_area("Data Set 2", height=400, key="ds2_input")
    with fields_columns[2]:
        combined_str = st.text_input(
            "Combined Delimiter (Optional)", key="combined_str_input"
        )

    if ds1_input and ds2_input:
        with fields_columns[2]:
            output = ""
            for line1 in split(ds1_input):
                for line2 in split(ds2_input):
                    output += line1 + combined_str + line2 + "\n"

            st.write("Result")
            st.code(output, language="python")


def _clear_inputs():
    st.session_state.ds1_input = ""
    st.session_state.ds2_input = ""
    st.session_state.combined_str_input = ""


def _show_example():
    st.session_state.ds1_input = "aa\nbbb"
    st.session_state.ds2_input = "ccc\nddd"


if __name__ == "__main__":
    show_combined()
