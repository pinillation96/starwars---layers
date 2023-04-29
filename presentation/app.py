import os
from flask import Flask, jsonify, request
import requests

from business_logic import movies

app = Flask(__name__)

movie_url = "https://swapi.dev/api/films/"


@app.route("/", methods=['GET'])
def list_movies():
    data = requests.get(movie_url).json()
    sorted_movies = movies.sort_movies_by_id(data["results"])
    return jsonify(sorted_movies)


@app.route("/characters/<int:movie_id>", methods=['GET'])
def list_movie_characters(movie_id):
    data = requests.get(f"{movie_url}{movie_id}/").json()
    character_names = movies.get_movie_character_names(data)
    return jsonify(character_names)


if __name__ == "__main__":
    port = int(os.environ['PORT'])
    app.run(host="0.0.0.0", debug=True, port=port)