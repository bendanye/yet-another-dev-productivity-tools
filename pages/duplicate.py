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
        selected_result_option = left.radio(
            "Result by",
            ["Whole Line", "Index"],
            index=1,
        )
        if split_str and index and enter_list and selected_result_option:
            output = ""
            if selected_result_option == "Index":
                unique_lines = set()
                for item in enter_list.split("\n"):
                    split_item = item.split(split_str)[int(index)]
                    if split_item in unique_lines:
                        output += split_item + "\n"

                    unique_lines.add(split_item)

            elif selected_result_option == "Whole Line":
                dict = {}
                for item in enter_list.split("\n"):
                    split_item = item.split(split_str)[int(index)]
                    records = dict.get(split_item, [])
                    records.append(item)
                    dict[split_item] = records

                for key in dict:
                    if len(dict[key]) > 1:
                        for item in dict[key]:
                            output += item + "\n"

            if output == "":
                output = "No duplicate"
            col3.code(output, language="python")


if __name__ == "__main__":
    show_duplicate()
