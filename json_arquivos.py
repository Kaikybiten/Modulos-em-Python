import json
import os

print(os.path.dirname(__file__))

json_dict = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'year': 2001,
    'budget': None
}

CAMINHO_JSON = os.path.join(os.path.dirname(__file__), 'json_arquivo.json')

with open(CAMINHO_JSON, "w")as arquivo_json:
    json.dump(json_dict, arquivo_json, ensure_ascii=False, indent=4)
