import sys
from random import randint
import statistics
from app import omdb_api
from app.generate_website import generate_html


def get_movie_name(message):
    """Prompt the user to enter a movie title, ensuring it is not empty."""
    while True:
        title = input(message)
        if len(title) != 0:
            break
        print("Movie name must not be empty")
    return title


def get_movie_year(message, can_blank=False):
    """Prompt the user to enter a movie year, with an option to leave it blank."""
    while True:
        try:
            year = input(message)
            if can_blank and len(year) == 0:
                return None
            return int(year)
        except ValueError:
            print("Please enter a valid year")


def get_movie_rating(message, can_blank=False):
    """Prompt the user to enter a movie rating between 1 and 10,
     with an option to leave it blank."""
    while True:
        try:
            rating = input(message)
            if can_blank and len(rating) == 0:
                return None
            if 1 <= float(rating) <= 10:
                return float(rating)
        except ValueError:
            print("Please enter a valid rating")


def get_reverse_value():
    """Prompt the user to choose if the list should be sorted in descending order."""
    reverse_value = {'N': False, 'Y': True}
    while True:
        sort_order = input("Do you want the latest movies first? (Y/N)")
        if sort_order not in reverse_value:
            print('Please enter "Y" or "N"')
            continue
        break
    return reverse_value[sort_order]


def is_substring(title, search):
    """Check if the search string is a substring of the movie title (case-insensitive)."""
    length_title = len(title)
    length_search = len(search)
    if length_search > length_title:
        return False
    char_pos = 0
    title = title.lower()
    search = search.lower()
    while char_pos < length_title:
        if title[char_pos:char_pos + length_search] == search:
            return True
        char_pos += 1
    return False


def get_rating(movie):
    """Retrieve the rating from a movie dictionary."""
    return movie['rating']


def print_movies(message, movies, amount):
    """Print a message followed by the list of movies and their rating."""
    print(message, end=" ")
    for movie in movies:
        print("{},".format(movie['title']), end=" ")
    print(amount)


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        """List all movies stored in the database."""
        print(self._storage)

    def _command_add_movie(self):
        """Add a new movie to the database."""
        title = get_movie_name('Enter new movie name: ')
        try:
            year, rating, poster, imdb_id, country = omdb_api.get_movie_info(title)
            if self._storage.add_movie(title, year, rating, poster, imdb_id, country):
                print(f"Movie {title} successfully added")
            else:
                print(f"Movie {title} already exist!")
        except ValueError as e:
            print(e)

    def _command_update_movie(self):
        """update a movie from the database by title.Add note to the movie"""
        title = get_movie_name('Enter movie name to update: ')
        note = input('Enter movie note to update: ')
        print(f"Movie {title} successfully updated") if self._storage.update_movie(title, note) \
            else print(f"Movie {title} doesn't exist!")

    def _command_delete_movie(self):
        """Delete a movie from the database by title."""
        title = get_movie_name('Enter movie name to delete: ')
        print(f"Movie {title} successfully deleted") if self._storage.delete_movie(title) \
            else print(f"Movie {title} doesn't exist!")

    def _command_random_movie(self):
        """Select and display a random movie from the database."""
        random_index = randint(0, len(self._storage.movies) - 1)
        random_movie_info = self._storage.movies[random_index]
        print(f"Your movie for tonight: {random_movie_info["title"]}, it's rated {random_movie_info["rating"]}")

    def _command_search_movie(self):
        """Search for movies containing a user-specified substring in their title."""
        search_title = get_movie_name("Enter part of movie name: ")
        match_movie_list = []
        for movie in self._storage.movies:
            if is_substring(movie["title"], search_title):
                match_movie_list.append(movie)
                print("{}, {}".format(movie["title"], movie["rating"]))
        if len(match_movie_list) == 0:
            print("There isn't any movies with this name")

    def _command_movie_sorted_by_rating(self):
        """List all movies sorted by rating."""
        self._storage.filter_method = "rating"
        self._storage.reverse_value = True
        self._storage.list_movies()
        print(self._storage)

    def _command_movie_stats(self):
        """Calculate and display statistical information about the movie database."""
        if not self._storage.movies:
            raise ValueError('No statistics data for empty Movies list')
        median = round(statistics.median(list(map(get_rating, self._storage.movies))), 2)
        sum_rating = sum(list(map(get_rating, self._storage.movies)))
        count_movie = len(self._storage.movies)
        avg = round(sum_rating / count_movie, 2)
        max_rating = max(list(map(get_rating, self._storage.movies)))
        min_rating = min(list(map(get_rating, self._storage.movies)))
        best_movies = [movie for movie in self._storage.movies if movie['rating'] == max_rating]
        worst_movies = [movie for movie in self._storage.movies if movie['rating'] == min_rating]
        print(f"Average rating: {avg}")
        print(f"Median rating: {median}")
        print_movies("Best movie:", best_movies, max_rating)
        print_movies("Worst movie:", worst_movies, min_rating)

    def _command_generate_website(self):
        """Generate An Html file from all movies in the list"""
        try:
            generate_html(self._storage.movies)
            print('Website was generated successfully.')
        except Exception as e:
            print(e)

    def run(self):
        """run command line"""
        help_str = """
           Menu:
           0. Exit
           1. List movies
           2. Add movie
           3. Delete movie
           4. Update movie
           5. Stats
           6. Random movie
           7. Search movie
           8. Movies sorted by rating
           9. Generate website
           


           Enter choice (0-8): 
           """.strip()

        welcome = "********** My Movies Database **********"
        cmd_funcs = {
            "0": sys.exit,
            "1": self._command_list_movies,
            "2": self._command_add_movie,
            "3": self._command_delete_movie,
            "4": self._command_update_movie,
            "5": self._command_movie_stats,
            "6": self._command_random_movie,
            "7": self._command_search_movie,
            "8": self._command_movie_sorted_by_rating,
            "9": self._command_generate_website
        }
        print(welcome)
        while True:
            print(help_str)
            cmd = input()

            # Execute the corresponding function based on user input
            if cmd in cmd_funcs:
                if cmd == "0":
                    print("Bye!")
                try:
                    cmd_funcs[cmd]()
                except Exception as e:
                    print(e)

            else:
                print("Invalid choice")
            input("Press Enter to continue...")
