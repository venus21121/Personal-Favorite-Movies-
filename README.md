# Personal-Favorite-Movies

This project allows users to store and manage their favorite movies. Users can add, view, and organize their movie list, along with additional details like ratings, genres, and movie poster images. This is a personal project to practice working with APIs, databases, and front-end technologies.

## Description
This project allows users to store, manage, and rate their favorite movies. Users can add movies to their collection, view details about them, and rate them. Additionally, based on the movies in their collection, the system can recommend similar movies. Users can also edit their ratings and reviews for their personal collection, enhancing their movie-watching experience.

The project uses the **TMDB API** to fetch detailed movie information, such as movie titles, ratings, poster images, and release years.

## Features
- **Add movies** to your personal collection with title, genre, and rating.
- **Edit or delete movies** from your collection.
- **Rate movies** and write reviews for your own collection.
- **Search for movies** by title.
- **Receive movie recommendations** based on the movies you've already added to your collection.
- **Edit your own ratings and reviews** after adding a movie to your collection.
- Display movie details such as **TMDB ratings**, poster, and release year.

## Technologies Used
- **Frontend:** HTML, Bootstrap
- **Backend:** Python, Flask 
- **Database:** SQLite
- **External API:** [TMDB API](https://www.themoviedb.org/documentation/api) for fetching movie details.

## Setting up the Environment
1. Clone the repository:
   ```bash
   git clone https://github.com/venus21121/Personal-Favorite-Movies.git
2. Navigate to project directory: 
   ```
   cd Personal-Favorite-Movies
3. Set up a virtual environment:
   ```
   python -m venv venv
4. Activate the virtual environment: 
   ```
   .\venv\Scripts\activate
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
6. Create a .env file in the root directory of the project and add your TMDB API key:
   ```bash 
   TMDB_API_KEY=your_api_key_here
7. Run Project:
   ```bash 
   python run.py