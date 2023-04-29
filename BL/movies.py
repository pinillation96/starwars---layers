def sort_movies_by_id(movies):
    return sorted(movies, key=lambda movie: movie["episode_id"])


def get_movie_character_names(movie_data):
    characters = []
    for url in movie_data["characters"]:
        character_data = requests.get(url).json()
        characters.append(character_data["name"])
    return characters