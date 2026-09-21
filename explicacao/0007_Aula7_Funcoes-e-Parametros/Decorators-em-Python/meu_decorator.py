import time

import requests


def calcular_tempo(funcao):
    def wrapper():
        inicio = time.time()
        funcao()
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"A duração foi de {tempo_execucao} segundos")
    return wrapper

@calcular_tempo
def pegar_cotacao_dolar():
    link = "https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])

pegar_cotacao_dolar()