import streamlit as st
import re


def show_template():
    st.title("Template")

    st.write(
        "Enter lines and a template contains {REPLACE} and each line will get replace."
    )
    st.write(
        "Additional: if the template contains {INCREMENT_NUM_FROM_<NUMBER>}, it will get increment from the specify "
        "number."
    )

    col1, col2 = st.columns(2)

    enter_lines = col1.text_area("Lines", height=300)

    enter_template = col2.text_area("Template", height=200)

    if enter_lines and enter_template:
        increment = -1
        increment_num_from_str = ""
        need_increment = False
        if "{INCREMENT_NUM_FROM_" in enter_template:
            increment = _extract_number(enter_template)
            increment_num_from_str = "{INCREMENT_NUM_FROM_" + str(increment) + "}"
            need_increment = True

        output = ""
        for line in enter_lines.split("\n"):
            format_line = enter_template.replace("{REPLACE}", line)
            if need_increment:
                format_line = format_line.replace(
                    increment_num_from_str, str(increment)
                )
                increment += 1
            output += format_line + "\n\n"

        st.code(output, language="python")


def _extract_number(string):
    # Use regex to find the number between angle brackets <>
    match = re.search(r"{INCREMENT_NUM_FROM_(\d+)}", string)
    if match:
        return int(match.group(1))
    else:
        raise ValueError("No number found in the string.")


if __name__ == "__main__":
    show_template()
