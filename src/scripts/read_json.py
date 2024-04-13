import json
from .write_json import write_to_json_file


async def read_json_file(filepath: str):
    """
    Asynchronous function, that: Reads the content from the file.
        - If the file doesn't exist - creates it with empty dict as content
        - If json.decoder.JSONDecodeError occurs - creates a new file with empty dict as content

    :return (dict): the content of the file

    """
    try:
        with open(filepath) as file:
            return json.load(file)
    except FileNotFoundError:
        await write_to_json_file(content={}, filepath=filepath)
        return {}
    except json.decoder.JSONDecodeError:
        await write_to_json_file(content={}, filepath=filepath)
        return {}
