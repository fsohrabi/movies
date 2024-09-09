import json
import os
from storage.file_storage import FileStorage


class StorageJson(FileStorage):
    def load_data(self):
        """Loads movie data from a JSON file."""
        folder_name = 'data'
        self.file_path = os.path.join(folder_name, self.file_path)
        directory = os.path.dirname(self.file_path)
        # Check if the directory exists, if not, create it
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as handle:
                    return json.load(handle)  # Directly load from the file
            except json.JSONDecodeError:
                # Handle the case where the file exists but contains invalid JSON
                print(f"Error: Corrupted JSON file at {self.file_path}. Resetting data.")
                return []
        else:
            with open(self.file_path, "w") as handle:
                json.dump([], handle)  # Write an empty list to the file
            return []

    def rewrite_data(self):
        """Write the updated movie data back to the JSON storage."""
        try:
            with open(self.file_path, "w") as handle:
                json.dump(self.movies, handle, indent=4)  # Indentation for readability
        except Exception as e:
            print(f"Error writing to file: {e}")
