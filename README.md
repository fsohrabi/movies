# My Movie App

A command-line application for managing a movie database, which includes functionalities to add, delete, update, and search movies, as well as generate a movie listing website.

## Features

- **Add Movies:** Add new movies to the database with title, year, rating, poster, IMDb ID, and country.
- **List Movies:** Display all movies in the database.
- **Delete Movies:** Remove movies from the database by title.
- **Update Movies:** Add notes to existing movies.
- **Search Movies:** Find movies by part of their title.
- **Random Movie:** Get a random movie recommendation.
- **Sort Movies:** List movies sorted by rating.
- **Statistics:** View average, median, highest, and lowest ratings.
- **Generate Website:** Create a static HTML file with a styled movie list.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/fsohrabi/movies.git
    ```

2. Change directory to the project folder:
    ```bash
    cd movies
    ```

3. Install dependencies (if applicable):
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file with your OMDB API key:
    ```env
    API_KEY=your_omdb_api_key
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py -n your_file_name.json
    ```

2. **Interact with the application:**
   Follow the prompts to use different functionalities such as adding movies, listing them, etc.

## Commands

- **0:** Exit the application
- **1:** List all movies
- **2:** Add a new movie
- **3:** Delete a movie
- **4:** Update a movie
- **5:** Show movie statistics
- **6:** Get a random movie recommendation
- **7:** Search for movies by title
- **8:** List movies sorted by rating
- **9:** Generate a movie listing website

## License

This project is licensed under the MIT License.
