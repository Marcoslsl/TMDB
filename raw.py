from src.drivers.requester_spy import RequesterSpy
from src.stages.extract import ExtractMovies
from src.stages.transform import Tranformer
import requests
import json
import pprint

# url = "https://api.themoviedb.org/3/movie/11?api_key=a773e9c7af7861e875f8f9d6ada80d36"
# headers = {"accept": "application/json"}
#
# r = []
#
# for movie_id in range(2, 5 + 2):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=a773e9c7af7861e875f8f9d6ada80d36"
#     response = requests.get(url, headers=headers)
#     r.append(response.json())

# with open("data.json", "w") as file:
#    json.dump(r, file)

# pprint.pprint(response.json())

api_key = "teste"
ex = ExtractMovies(api_key, RequesterSpy)
data = ex.extract(qtd_movies=2)
data = Tranformer().transform(data)
pprint.pprint(data)
