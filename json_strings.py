import json
from pprint import pprint

json_string = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}'''

# Carregando a string em json para um dicionario, e convertendo para linguagem
# python
filme = json.loads(json_string)
pprint(filme)
print()

# Carregando o dicionario em python para uma string, e convertendo para
# linguagem json
filme_dump = json.dumps(
    filme, ensure_ascii=False,  # Criptografia com acentos
    indent=2  # Identando a string
)
pprint(filme_dump)
