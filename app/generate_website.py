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
          <li class="movie-item">
              <div class="movie">
                  <img class="movie-poster" src="{movie['poster']}" alt="{movie['title']}" title="{movie['note']}">
                  <div class="movie-title">{movie['title']}</div>
                  <div class="movie-year">{movie['year']}</div>
              </div>
          </li>
          '''
        movie_grid_html += movie_html

    template = template.replace('__TEMPLATE_MOVIE_GRID__', movie_grid_html)
    html_movie_file_path = os.path.join(folder_name, HTML_MOVIE_PATH)
    with open(html_movie_file_path, 'w') as file:
        file.write(template)
