import yaml

from typing import List


def compare_yaml_by_content(source_content: str, to_compare_content: str):
    source_key_paths = _get_key_paths_from_content(source_content)
    to_compare_key_paths = _get_key_paths_from_content(to_compare_content)

    missing_from_source = [x for x in source_key_paths if x not in to_compare_key_paths]
    extra_from_to_compare = [
        x for x in to_compare_key_paths if x not in source_key_paths
    ]
    return missing_from_source, extra_from_to_compare


def compare_yaml_by_files(source_file_path: str, to_compare_file_path: str):
    source_key_paths = _get_key_paths_from_file(source_file_path)
    to_compare_key_paths = _get_key_paths_from_file(to_compare_file_path)

    missing_from_source = [x for x in source_key_paths if x not in to_compare_key_paths]
    extra_from_to_compare = [
        x for x in to_compare_key_paths if x not in source_key_paths
    ]
    return missing_from_source, extra_from_to_compare


def _get_key_paths_from_content(content: str) -> List[str]:
    data = yaml.safe_load(content)
    return _generate_key_paths(data)


def _get_key_paths_from_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
        return _generate_key_paths(data)


def _generate_key_paths(d, parent_key="") -> List[str]:
    paths = []
    for k, v in d.items():
        new_key = f"{parent_key}.{k}" if parent_key else k
        if isinstance(v, dict):
            paths.extend(_generate_key_paths(v, new_key))
        else:
            paths.append(new_key)
    return paths
