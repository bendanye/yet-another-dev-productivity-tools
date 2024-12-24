import streamlit as st
import time
import pexpect


def show_command_polling():
    st.title("Command Polling")
    st.write("This tool is to keep running the same command until it stopped")

    if "clicked" not in st.session_state:
        st.session_state.clicked = False

    command = st.text_input("Command")
    wait_seconds = st.text_input("Wait for how many second(s) before rerun command")
    output_file = st.text_input(
        "File to create/append containing the output of the command"
    )

    if st.session_state.clicked:
        st.button("Stop", on_click=click_button)
    else:
        st.button("Poll", on_click=click_button)

    if command and wait_seconds:
        while st.session_state.clicked:
            if output_file:
                with open(output_file, "ab") as file:
                    pexpect.run(command, logfile=file)
            else:
                output = pexpect.run(command)
                st.code(output, language="python")

            st.code(
                f"Wait for {wait_seconds} seconds before rerun the command",
                language="python",
            )

            time.sleep(int(wait_seconds))


def click_button():
    if st.session_state.clicked:
        st.session_state.clicked = False
    else:
        st.session_state.clicked = True


if __name__ == "__main__":
    show_command_polling()
