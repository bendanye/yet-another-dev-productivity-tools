import streamlit as st


def show_vlookup():
    st.title("Vlookup")
    st.write(
        "This tool is to replicate the Excel vlookup without having enter those formula"
    )

    columns = st.columns([1, 6])
    with columns[0]:
        st.button("Clear", on_click=_clear_inputs)
    with columns[1]:
        st.button("Show Inputs Example", on_click=_show_example)

    fields_columns = st.columns([3, 3, 3, 3])
    with fields_columns[0]:
        lines_input = st.text_area("Data Set 1", height=400, key="lines_input")
    with fields_columns[1]:
        criteria_input = st.text_area("Criteria", height=400, key="criteria_input")
    with fields_columns[2]:
        split_str = st.text_input("Split Str", key="split_str_input")
        search_by_input = st.text_input("Search By", key="search_by_input")

    if lines_input and criteria_input and split_str and search_by_input:
        with fields_columns[3]:
            output = ""

            results = _get_line_that_matches(
                lines_input=lines_input,
                criteria_input=criteria_input,
                split_str=split_str,
                search_by_input=search_by_input,
            )

            for line in results:
                for col in line:
                    output += f"{col}{split_str}"
                output += "\n"

            st.write("Result")
            st.code(output, language="python")


def _to_array(input: str, split_str: str):
    return [line.split(split_str) for line in input.split("\n")]


def _col_index(inputs, search_by_input):
    for index, item in enumerate(inputs[0]):
        if item == search_by_input:
            return index

    return -1


def _get_line_that_matches(lines_input, criteria_input, split_str, search_by_input):
    lines = _to_array(input=lines_input, split_str=split_str)
    lines_index = _col_index(lines, search_by_input)

    criterias = _to_array(input=criteria_input, split_str=split_str)
    criteria_index = _col_index(criterias, search_by_input)

    result = []
    result.append(lines[0])

    for criteria in criterias[1:]:
        for line in lines[1:]:
            if line[lines_index] == criteria[criteria_index]:
                result.append(line)

    return result


def _clear_inputs():
    st.session_state.lines_input = ""
    st.session_state.criteria_input = ""
    st.session_state.split_str_input = ""
    st.session_state.search_by_input = ""


def _show_example():
    st.session_state.lines_input = "email;name;address\njohn@test.com;john walker;abc\npeter@test.com;peter park;abc"
    st.session_state.criteria_input = "email;order\njohn@test.com;apple"
    st.session_state.split_str_input = ";"
    st.session_state.search_by_input = "email"


if __name__ == "__main__":
    show_vlookup()
