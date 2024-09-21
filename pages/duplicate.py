import streamlit as st


def show_duplicate():
    st.title("Duplicate")
    st.write("This tool is to get list of duplicate")

    col1, col2, col3 = st.columns(3)

    enter_list = col1.text_area("List", height=500)
    selected_option = col2.radio(
        "Checked by",
        ["Whole Line", "Index"],
        index=None,
    )

    if selected_option == "Whole Line":
        if enter_list:
            output = ""
            unique_lines = set()
            for item in enter_list.split("\n"):
                if item in unique_lines:
                    output += item + "\n"

                unique_lines.add(item)

            if output == "":
                output = "No duplicate"
            col3.code(output, language="python")
    elif selected_option == "Index":
        left, right = col2.columns(2)
        split_str = left.text_input("Split Str")
        index = right.text_input("Index to get")
        if split_str and index and enter_list:
            output = ""
            unique_lines = set()
            for item in enter_list.split("\n"):
                split_item = item.split(split_str)[int(index)]
                if split_item in unique_lines:
                    output += split_item + "\n"

                unique_lines.add(split_item)

            if output == "":
                output = "No duplicate"
            col3.code(output, language="python")


if __name__ == "__main__":
    show_duplicate()
