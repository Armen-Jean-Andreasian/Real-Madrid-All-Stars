import json


async def write_to_json_file(content: dict | list, filepath: str):
    """
    Asynchronous function, that: Dump content to filepath.
    :return: None
    """
    with open(filepath, 'w') as file:
        json.dump(content, file, indent=4)
