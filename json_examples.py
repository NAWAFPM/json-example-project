import json

# Example 1: Movie
movie = {"title": "kgf", "year": 2020, "genre": "action"}
movie_json = json.dumps(movie)
print(movie_json)

movie_dict = json.loads(movie_json)
print(movie_dict["year"])

# Example 2: Song
song = {"title": "munthirichar", "artist": "mhr"}
song_json = json.dumps(song)
print(song_json)

song_dict = json.loads(song_json)
print(song_dict["artist"])
