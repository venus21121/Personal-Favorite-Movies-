# Utility functions for shared logic

def extract_genres(movie_data):
    if 'genres' in movie_data:
        return ', '.join([str(genre['id']) for genre in movie_data['genres']])  # Convert genre IDs to strings
    if 'genre_ids' in movie_data:
        return ", ".join( str(genre_id) for genre_id in movie_data['genre_ids'])
    return "Unknown"
