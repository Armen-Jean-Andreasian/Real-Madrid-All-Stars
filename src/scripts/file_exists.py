import os


def file_exists(filepath: str) -> bool:
    """Checks if the file exists"""
    return os.path.exists(filepath)
