import os
import csv
from storage.file_storage import FileStorage


class StorageCsv(FileStorage):
    def load_data(self):
        """ Loads data from a CSV file """
        folder_name = 'data'
        self.file_path = os.path.join(folder_name, self.file_path)
        if os.path.exists(self.file_path):
            with open(self.file_path, mode='r') as handle:
                reader = csv.DictReader(handle)
                return [row for row in reader]  # Load rows as list of dicts
        # If file does not exist, create it and return an empty list
        with open(self.file_path, mode='w', newline='') as handle:
            pass
        return []

    def rewrite_data(self):
        """ Write the updated movie data back to CSV storage. """
        with open(self.file_path, mode='w', newline='') as handle:
            fieldnames = ['title', 'year', 'rating', 'poster']
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()  # Write header
            writer.writerows(self.movies)  # Write all movies at once
