# Códigos status HTTP
# 1XX -> informacionais
# 2xx -> requisição deu certo
# 200 -> OK
# 201 -> CREATED
# 202 -> ACCEPTED
# 204 -> NO CONTENT
# 3XX -> isso que você ta procurando, não está aqui
# 301 -> esse link foi permanentemente redirecionado
# 302 -> redirecionamento que pode ser temporário
# 4XX -> erro do lado do cliente
# 400 -> Bad request (está mandando alguma coisa no formato errado)
# 401 -> Unauthorized
# 403 -> Forbidden
# 404 -> Página não encontrada
# 405 -> method not allowed
# 5XX -> erro do lado do servidor
# 500 -> erro interno no servidor (genérico)
# 501 -> erro not implemented yet
# 502 -> Bad Gateway
# 503 -> Service Unavaiable
import requests

requisicao = requests.get(
    "http://127.0.0.1:5000/postar_foto")

print(requisicao)
print(requisicao.reason)