from typing import List


def split(line_input: str, delimiter: str = "\n") -> List[str]:
    arr = line_input.split(delimiter)
    return [item for item in arr if item]
