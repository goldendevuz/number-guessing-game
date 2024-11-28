import json
from typing import Any, Dict, Union


class JsonHandler:
    def __init__(self, file_path: str = "tasks.json") -> None:
        self.file_path: str = file_path

    def read(self) -> Dict[str, Any]:
        """Reads the JSON file and returns its contents as a dictionary."""
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def write(self, key: int, value: Dict[str, Any]) -> None:
        """Writes a key-value pair to the JSON file."""
        data: Dict[str, Any] = self.read()
        data[str(key)] = value
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def update(self, key: int, value: Dict[str, Any]) -> None:
        """Updates an existing key with new data in the JSON file."""
        data: Dict[str, Any] = self.read()
        key_str: str = str(key)
        if key_str in data:
            data[key_str].update(value)
            with open(self.file_path, "w") as f:
                json.dump(data, f, indent=4)

    def delete(self, key: int) -> None:
        """Deletes a key-value pair from the JSON file."""
        data: Dict[str, Any] = self.read()
        key_str: str = str(key)
        if key_str in data:
            del data[key_str]
            with open(self.file_path, "w") as f:
                json.dump(data, f, indent=4)
