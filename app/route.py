# Route handlers
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Movie, UserComment
from . import db
from .services import fetch_movie_details, fetch_recommendations
from .utils import extract_genres

main_bp = Blueprint('main', __name__)
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


@main_bp.route('/')
def home():
    movies = Movie.query.order_by(Movie.rating.desc()).all()
    for i, movie in enumerate(movies, start=1):
        movie.ranking = i
    db.session.commit()

    if movies:
        top_genres = []
        for movie in movies[:5]:
            top_genres.extend(movie.genres.split(", "))

        top_genres = sorted(set(top_genres), key=top_genres.count, reverse=True)
        print("top_genres", top_genres)
        recommendations = fetch_recommendations(top_genres)
    else:
        recommendations = []

    return render_template('home.html', movies=movies, recommendations=recommendations)

@main_bp.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        query = request.form.get('movie_title')
        results = fetch_movie_details(query=query)

        if results:
            return render_template('addMovie.html', movies=results)
        else:
            return render_template('addMovie.html', error="No movies found.")

    return render_template('addMovie.html')

@main_bp.route('/select_movie', methods=['POST'])
def select_movie():
    movie_id = request.form.get('movie_id')

    if not movie_id:
        return "Movie ID is missing.", 400
    try:
        movie_data = fetch_movie_details(movie_id=movie_id)

        if not movie_data:
            return "Error fetching movie details.", 500

        existing_movie = Movie.query.filter_by(title=movie_data['title']).first()
        if existing_movie:
            return render_template('edit_movie.html', movie=existing_movie)

        genres_string = extract_genres(movie_data)
        new_movie = Movie(
            title=movie_data.get('title', 'Unknown Title'),
            release_year=movie_data.get('release_date', 'Unknown Date').split('-')[0],
            description=movie_data.get('overview', 'No description available'),
            genres=genres_string,
            vote_average=movie_data.get('vote_average', 0.0),
            img_url=f"{MOVIE_DB_IMAGE_URL}{movie_data.get('poster_path', '')}",
        )
        db.session.add(new_movie)
        db.session.commit()

        return render_template('edit_movie.html', movie=new_movie)
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}", 500


@main_bp.route('/edit_movie/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie = Movie.query.get_or_404(id)

    if request.method == 'POST':
        movie.rating = request.form['rating']
        movie.review = request.form['review']
        db.session.commit()
        return redirect(url_for('main.home'))

    return render_template('edit_movie.html', movie=movie)

@main_bp.route('/delete_movie/<int:id>')
def delete_movie(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('main.home'))
