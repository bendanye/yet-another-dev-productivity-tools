import streamlit as st

from pages.splitter import split


def show_conversion():
    st.title("Conversion")
    st.write("This tool is to help to transform each line of string to selected option")

    col1, col2, col3 = st.columns(3)

    enter_list = col1.text_area("List", height=500)
    selected_option = col2.radio(
        "Option",
        [
            "Single Quotes",
            "Double Quotes",
            "Bash Array",
            "SQL IN Params",
            "Key Value",
            "Bash Env Var",
            "Bash Env Var (Export)",
            "Ansible Values",
            "Spring Boot Env Var",
            "Lines Break",
            "Single Line with Line Break",
            "Remove extra Line Break",
        ],
        index=None,
    )

    if enter_list:
        if selected_option == "Single Quotes":
            output = ""
            for item in split(enter_list):
                format_item = f"'{item}',"
                output += format_item + "\n"

            col3.code(output, language="python")

        elif selected_option == "Double Quotes":
            output = ""
            for item in split(enter_list):
                format_item = f'"{item}",'
                output += format_item + "\n"

            col3.code(output, language="python")

        elif selected_option == "Bash Array":
            output = "("
            for item in split(enter_list):
                format_item = f'"{item}" '
                output += format_item

            output = output[:-1]
            output += ")"

            col3.code(output, language="bash", wrap_lines=True)

        elif selected_option == "SQL IN Params":
            output = "("
            for item in split(enter_list):
                format_item = f"'{item}', "
                output += format_item

            output = output[:-2]
            output += ")"

            col3.code(output, language="bash", wrap_lines=True)

        elif selected_option == "Key Value":
            output = ""
            for item in split(enter_list):
                format_item = f'"{item}": "",'
                output += format_item + "\n"

            col3.code(output, language="python")

        elif selected_option == "Single Line with Line Break":
            output = ""
            for item in split(enter_list):
                format_item = f"{item}\\n"
                output += format_item

            output = output[:-2]
            col3.code(output, language="python")

        elif selected_option == "Bash Env Var":
            output = ""
            for item in split(enter_list):
                format_item = item.replace(".", "_").upper()
                output += format_item + "\n"

            output = output[:-1]
            col3.code(output, language="python")

        elif selected_option == "Bash Env Var (Export)":
            output = ""
            for item in split(enter_list):
                format_item = item.replace(".", "_").upper()
                output += "export " + format_item + "\n"

            output = output[:-1]
            col3.code(output, language="python")

        elif selected_option == "Ansible Values":
            output = ""
            for item in split(enter_list):
                format_item = '"{{ ' + item + ' }}"'
                output += format_item + "\n"

            col3.code(output, language="python")

        elif selected_option == "Spring Boot Env Var":
            output = ""
            for item in split(enter_list):
                format_item = item.replace("_", ".").lower()
                output += format_item + "\n"

            output = output[:-1]
            col3.code(output, language="python")

        elif selected_option == "Lines Break":
            output = ""
            for item in split(enter_list):
                if "\\n" in item:
                    for sub_item in item.split("\\n"):
                        output += sub_item + "\n"
                else:
                    output += item + "\n"

            col3.code(output, language="python")
        elif selected_option == "Remove extra Line Break":
            output = ""
            for item in split(enter_list):
                if item != "\n":
                    output += item.strip() + "\n"

            col3.code(output, language="python")


if __name__ == "__main__":
    show_conversion()
