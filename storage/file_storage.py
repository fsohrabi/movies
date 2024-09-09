from storage.istorage import IStorage


class FileStorage(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self.movies = self.load_data()  # Load existing data
        self._filter_method = None
        self._reverse_value = False

    @property
    def filter_method(self):
        return self._filter_method

    @filter_method.setter
    def filter_method(self, filter_method):
        self._filter_method = filter_method

    @property
    def reverse_value(self):
        return self._reverse_value

    @reverse_value.setter
    def reverse_value(self, reverse_value):
        self._reverse_value = reverse_value

    def load_data(self):
        raise NotImplementedError("Subclasses must override load_data.")

    def rewrite_data(self):
        raise NotImplementedError("Subclasses must override rewrite_data.")

    def list_movies(self):
        """Retrieve and optionally filter or sort movies from the database."""
        if self.filter_method:
            self.movies = sorted(self.movies, key=lambda item: item['rating'], reverse=self.reverse_value)
        return self.movies

    def add_movie(self, title, year, rating, poster, imdb_id, country):
        """Add a new movie to the database."""
        for movie in self.movies:
            if movie['title'] == title:
                return False  # Duplicate movie title
        self.movies.append(
            {'title': title, 'year': year, 'rating': rating, 'poster': poster, 'note': '', 'imdb_id': imdb_id,
             'country': country})
        self.rewrite_data()
        return True

    def update_movie(self, title, note):
        """update movie from the database."""
        for movie in self.movies:
            if movie['title'] == title:
                movie['note'] = note
                self.rewrite_data()
                return True
        return False

    def delete_movie(self, title):
        """Delete a movie from the database by title."""
        for movie in self.movies:
            if movie['title'] == title:
                self.movies.remove(movie)
                self.rewrite_data()  # Persist changes
                return True
        return False

    def __str__(self):
        """Print the list of movies with their title, year, and rating."""
        total = len(self.movies)
        print_string = f'{total} movies in total\n'
        for movie in self.movies:
            print_string += f"{movie['title']} ({movie['year']}): {movie['rating']}\n"
        return print_string
