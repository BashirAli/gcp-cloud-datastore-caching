import json

from model.logging import logger


def load_json_file(file_path) -> list[dict] | list[None]:
    try:
        # Open and read the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        logger.info(f"Error: The file '{file_path}' does not exist.")
        return []
    except json.JSONDecodeError as e:
        logger.info(f"Error decoding JSON from the file '{file_path}': {e}")
        return []
