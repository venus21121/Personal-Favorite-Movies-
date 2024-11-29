# API interaction and business logic
from decouple import config
import requests
MOVIE_DB_API_KEY = config('API_KEY')
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_DISCOVER_MOVIE_URL = "https://api.themoviedb.org/3/discover/movie"

def fetch_movie_details(query=None, movie_id=None):
    params = {"api_key": MOVIE_DB_API_KEY, "language": "en-US"}
    url = MOVIE_DB_SEARCH_URL if query else MOVIE_DB_INFO_URL + f"/{movie_id}"

    if query:
        params['query'] = query

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json().get('results') if query else response.json()

def fetch_recommendations(genre_ids):
    params = {
        "api_key": MOVIE_DB_API_KEY,
        "language": "en-US",
        "with_genres": ",".join(genre_ids),
        "sort_by": "popularity.desc"
    }

    response = requests.get(MOVIE_DB_DISCOVER_MOVIE_URL, params=params)
    return response.json().get('results', [])
