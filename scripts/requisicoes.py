import requests

url = 'http://127.0.0.1:5000/filmes'


# resposta = requests.get(url)

# dados = resposta.json()
# print(dados)

# novo = {
#     'titulo': 'Django Livre',
#     'ano': 2012,
#     'genero': 'Ação'
# }

# resposta = requests.post(url, json=novo)
# print(resposta.status_code)
# print(resposta.json())

# dados = resposta.json()
# print(dados)

# dados = {
#     'titulo': 'Devorador de Estrelas',
#     'ano': 2026,
#     'genero': 'Ficção'
# }

# id_string = '/2' # id que vamos mudar

# resposta = requests.put(url + id_string, json=dados)
# print(resposta.status_code)
# print(resposta.json())


# dados = {
#     'genero': 'Ficção científica'
# }

# id_string = '/2' # id que vamos mudar

# resposta = requests.patch(url + id_string, json=dados)
# print(resposta.status_code)
# print(resposta.json())



id_string = '/2' # id que vamos mudar

resposta = requests.delete(url + id_string)
print(resposta.status_code)
print(resposta.json())