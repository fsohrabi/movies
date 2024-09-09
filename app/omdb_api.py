import os
from dotenv import load_dotenv
import requests


def get_movie_info(title):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    url = 'http://www.omdbapi.com/?apikey=' + api_key + '&t=' + title
    response = requests.get(url)
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        response.raise_for_status()
        json_response = response.json()
        # Check if the movie was found (OMDb uses the 'Response' field)
        if json_response.get('Response') == 'False':
            raise ValueError(f"{json_response.get('Error', 'Unknown error')}")

        # Extracting the necessary fields
        year = json_response.get('Year', 'N/A')
        imdb_rating = json_response.get('imdbRating', 'N/A')
        poster = json_response.get('Poster', 'N/A')
        imdb_id = json_response.get('imdbID', 'N/A')
        country = json_response.get('Country', 'N/A')
        return int(year), float(imdb_rating), poster, imdb_id, country

    except requests.exceptions.HTTPError as http_err:
        raise ValueError(f"HTTP error occurred: {http_err}")  # API returned an error status code
    except requests.exceptions.ConnectionError:
        raise ValueError("Error connecting to the API. Please check your network connection.")
    except requests.exceptions.Timeout:
        raise ValueError("The request to the API timed out.")
    except requests.exceptions.RequestException as req_err:
        raise ValueError(f"An error occurred during the API request: {req_err}")
