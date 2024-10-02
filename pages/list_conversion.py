import streamlit as st

from pages.splitter import split


def show_list_conversion():
    st.title("List conversion")
    st.write("This tool is to help to transform each line of string to selected option")

    col1, col2, col3 = st.columns(3)

    enter_list = col1.text_area("List", height=500)
    selected_option = col2.radio(
        "Option",
        ["Double Quotes", "Bash Array", "Key Value", "Single Line with Line Break", "Bash Env Var", "Spring Boot Env Var"],
        index=None,
    )

    if enter_list:
        if selected_option == "Double Quotes":
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

        elif selected_option == "Spring Boot Env Var":
            output = ""
            for item in split(enter_list):
                format_item = item.replace("_", ".").lower()
                output += format_item + "\n"

            output = output[:-1]
            col3.code(output, language="python")

if __name__ == "__main__":
    show_list_conversion()
