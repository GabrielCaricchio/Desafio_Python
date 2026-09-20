import requests
import pprint

api_key = "59b44a9d51d54f299ff143040252603"
link_api = "http://api.weatherapi.com/v1/current.json"

parametros = {
    "key": api_key,
    "q": "Paris",
    "lang": "pt"
}

resposta = requests.get(link_api, params=parametros)

if resposta.status_code == 200:
    dados_requisicao = resposta.json()
    pprint.pprint(dados_requisicao)
    temp = dados_requisicao["current"]["temp_c"]
    descricao = dados_requisicao["current"]["condition"]["text"]
    print(temp)
    print(descricao)

# status code
# 200 -> deu certo a requisição
# 300 -> redirecionada
# 400 -> não conseguiu fazer a requisição
# 500 -> deu um erro no sistema