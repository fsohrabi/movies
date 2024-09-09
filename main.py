from app.movie_app import MovieApp
from storage.storage_json import StorageJson


def main():
    """Main function to display the menu and handle user input."""
    storage = StorageJson('movies.json')
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
