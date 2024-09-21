import streamlit as st


def show_compare_lists():
    st.title("Compare Lists")
    st.write(
        "This tool is to compare two lists and get the values from List 1 that is not found in List 2"
    )

    button_columns = st.columns([1, 6])
    with button_columns[0]:
        st.button("Switch", on_click=_switch_inputs)

    fields_columns = st.columns([3, 3, 3])
    with fields_columns[0]:
        list_1_input = st.text_area("List 1", height=400, key="input_1")
    with fields_columns[1]:
        list_2_input = st.text_area("List 2", height=400, key="input_2")

    if list_1_input and list_2_input:
        with fields_columns[2]:
            list_1 = [item for item in list_1_input.split("\n")]
            list_2 = [item for item in list_2_input.split("\n")]
            results = list(set(list_1) - set(list_2))
            if results:
                output = ""
                for item in results:
                    output += item + "\n"
            else:
                output = "No differences"

            st.write("Result")
            st.code(output, language="python")


def _switch_inputs():
    tmp = st.session_state.input_1
    st.session_state.input_1 = st.session_state.input_2
    st.session_state.input_2 = tmp


if __name__ == "__main__":
    show_compare_lists()
