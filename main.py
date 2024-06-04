from flask import Flask, render_template, request
import random

from movies_catalogue import tmdb_client
from tmdb_client import get_poster_url, get_movies_list, get_single_movie, get_single_movie_cast, get_movie_images

app = Flask(__name__)


LIST_TYPES = ['top_rated', 'upcoming', 'popular', 'now_playing']


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    results = data["results"][:how_many]
    random.shuffle(results)
    return results


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    if selected_list not in LIST_TYPES:
        selected_list = "popular"
    movies = get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, list_types=LIST_TYPES)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    return render_template("movie_details.html", movie=details)


if __name__ == "__main__":
    app.run(debug=True)