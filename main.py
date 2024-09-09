from app.movie_app import MovieApp
from storage.storage_json import StorageJson
import argparse


def main():
    """Main function to display the menu and handle user input."""
    parser = argparse.ArgumentParser(description='Get user filename to save movies')
    parser.add_argument('-n', '--name', type=str, required=True, help='name of file')
    args = parser.parse_args()
    storage = StorageJson(args.name)
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
