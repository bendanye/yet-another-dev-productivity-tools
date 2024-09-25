import streamlit as st

from pages.splitter import split


# Function to manage the app's state
def show_transformation():
    # Initialize session state
    if "rows" not in st.session_state:
        st.session_state.rows = []

    st.title("String Transformation")
    st.write(
        "This tool is to help to transform each line of string using commonly used string function such as replace, split"
    )

    enter_list = st.text_area("Enter your line(s)")

    output_text = enter_list

    # Button to add a new row
    if st.button("Add Row"):
        st.session_state.rows.append(len(st.session_state.rows))

    # Display rows with drop-down and delete button
    if st.session_state.rows:
        for i in st.session_state.rows:
            cols = st.columns([3, 1])
            with cols[0]:
                selected = st.selectbox(
                    f"Row {i + 1}",
                    ["Replace", "Split", "String After Last Character", "Break Lines"],
                    key=f"dropdown_{i}",
                )
                if selected == "Replace":
                    left, right = st.columns(2)
                    from_value = left.text_input("From", key=f"left_ {i + 1}")
                    to_value = right.text_input("To", key=f"right_ {i + 1}")

                    if from_value and output_text:
                        output = ""
                        for item in split(output_text):
                            output += item.replace(from_value, to_value) + "\n"

                        output_text = output.rstrip()

                elif selected == "Split":
                    left, right = st.columns(2)
                    split_str = left.text_input("Split Str", key=f"split_str_ {i + 1}")
                    index = right.text_input(
                        "Index to get", key=f"split_index_ {i + 1}"
                    )
                    if split_str and index and output_text:
                        output = ""
                        for item in split(output_text):
                            output += item.split(split_str)[int(index)] + "\n"

                        output_text = output.rstrip()

                elif selected == "String After Last Character":
                    left, right = st.columns(2)
                    char = left.text_input(
                        "Last Character", key=f"str_after_{i + 1}", max_chars=1
                    )
                    is_include_last_character = right.checkbox(
                        "Include the Last Character", key=f"split_str_ {i + 1}"
                    )
                    if char:
                        output = ""
                        for item in split(output_text):
                            value = item.rsplit(char, 1)[1]
                            if is_include_last_character:
                                value = char + value

                            output += value + "\n"

                        output_text = output.rstrip()

                elif selected == "Break Lines":
                    output = ""
                    for item in split(output_text):
                        if "\\n" in item:
                            for sub_item in item.split("\\n"):
                                output += sub_item + "\n"
                        else:
                            output += item + "\n"

                    output_text = output

            with cols[1]:
                if st.button(f"Delete Row {i + 1}", key=f"delete_{i}"):
                    st.session_state.rows.remove(i)
                    st.rerun()  # Refresh to update rows

    # Read-only text area
    st.text_area("Output", value=output_text, disabled=True)


if __name__ == "__main__":
    show_transformation()
