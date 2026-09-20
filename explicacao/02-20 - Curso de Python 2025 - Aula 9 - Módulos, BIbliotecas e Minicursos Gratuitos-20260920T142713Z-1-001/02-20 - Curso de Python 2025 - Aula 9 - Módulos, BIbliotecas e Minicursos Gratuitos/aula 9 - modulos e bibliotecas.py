# import os

# print(os.getcwd())

# lista_arquivos = os.listdir("arquivos")
# print(lista_arquivos)

# for nome_arquivo in lista_arquivos:
#     if "txt" in nome_arquivo:
#         if "22" in nome_arquivo:
#             os.rename(f"arquivos/{nome_arquivo}", f"arquivos/22/{nome_arquivo}")
#         elif "23" in nome_arquivo:
#             os.rename(f"arquivos/{nome_arquivo}", f"arquivos/23/{nome_arquivo}")

import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(link)
print(resposta)
dic_resposta = resposta.json()

for moeda in dic_resposta:
    dic_conversao_moeda = dic_resposta[moeda]
    valor_moeda = dic_conversao_moeda["bid"]
    print(moeda, valor_moeda)

# {'USDBRL': {'code': 'USD', 'codein': 'BRL', 'name': 'Dólar Americano/Real Brasileiro', 'high': '6.0432', 'low': '6.0322', 'varBid': '0.0004', 'pctChange': '0.01', 'bid': '6.0361', 'ask': '6.0391', 'timestamp': '1736462807', 'create_date': '2025-01-09 19:46:47'}, 
#  'EURBRL': {'code': 'EUR', 'codein': 'BRL', 'name': 'Euro/Real Brasileiro', 'high': '6.2228', 'low': '6.2151', 'varBid': '0.0039', 'pctChange': '0.06', 'bid': '6.2112', 'ask': '6.2267', 'timestamp': '1736462798', 'create_date': '2025-01-09 19:46:38'}, 
#  'BTCBRL': {'code': 'BTC', 'codein': 'BRL', 'name': 'Bitcoin/Real Brasileiro', 'high': '587240', 'low': '554034', 'varBid': '-23549', 'pctChange': '-4.02', 'bid': '561313', 'ask': '561646', 'timestamp': '1736462812', 'create_date': '2025-01-09 19:46:52'}}