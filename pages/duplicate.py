import streamlit as st


def show_duplicate():
    st.title("Duplicate")
    st.write("This tool is to get list of duplicate")

    col1, col2, col3 = st.columns(3)

    enter_list = col1.text_area("List", height=500)
    selected_option = col2.radio(
        "Checked by",
        ["Whole Line"],
        index=None,
    )

    if enter_list:
        if selected_option == "Whole Line":
            output = ""
            unique_lines = set()
            for item in enter_list.split("\n"):
                if item in unique_lines:
                    output += item + "\n"

                unique_lines.add(item)

            if output == "":
                output = "No duplicate"
            col3.code(output, language="python")


if __name__ == "__main__":
    show_duplicate()
