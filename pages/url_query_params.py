import streamlit as st


def show_url_query_params():
    st.title("URL Query Params")
    st.write("This tool is to breakdown the query params")

    col1, col2 = st.columns(2)

    enter_url = col1.text_input("URL")
    if enter_url:
        if "?" in enter_url:
            output = ""
            query_params = enter_url.split("?")[1].split("&")
            for query_param in query_params:
                output += query_param + "\n"
            col2.code(output, language="python")
        else:
            col2.code("No query params", language="python")


if __name__ == "__main__":
    show_url_query_params()
