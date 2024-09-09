import os

HTML_TEMPLATE_PATH = 'index_template.html'
HTML_MOVIE_PATH = 'movies.html'


def generate_html(movies):
    """Generate the HTML content for the movie list."""
    folder_name = 'static'
    template_file_path = os.path.join(folder_name, HTML_TEMPLATE_PATH)
    with open(template_file_path, 'r') as file:
        template = file.read()

    # Replace the title placeholder
    template = template.replace('__TEMPLATE_TITLE__', 'Fatemeh Movies Project')

    # Generate the movie list HTML
    movie_grid_html = ''
    for movie in movies:
        movie_html = f'''
        <div class="movie">
            <div class="tooltip">
                <a href="https://www.imdb.com/title/{movie['imdb_id']}/" target="_blank">
                    <img class="movie-poster" src="{movie['poster']}" alt="Movie Poster">
                </a>
                <span class="tooltiptext">{movie['note']}</span>
            </div>
            <div class="movie-info">
                <div class="movie-title">{movie['title']}</div>
                <div class="movie-details">
                    <span class="movie-year">{movie['year']}</span>
                    <span class="movie-rating">⭐ {movie['rating']}</span>
                </div>
            </div>
        </div>
        
          '''
        movie_grid_html += movie_html

    template = template.replace('__TEMPLATE_MOVIE_GRID__', movie_grid_html)
    html_movie_file_path = os.path.join(folder_name, HTML_MOVIE_PATH)
    with open(html_movie_file_path, 'w') as file:
        file.write(template)
