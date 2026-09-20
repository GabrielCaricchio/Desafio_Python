from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Meu site no Ar"

@app.route("/link_antigo")
def sumiu():
    return redirect(url_for("homepage"), code=302)

@app.route("/usuario/<id>")
def usuario(id):
    try:
        id = int(id)
        return f"Usuario {id} carregado com sucesso"
    except:
        return "Erro na requisicao", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    return "OK"

@app.route("/foto_usuario/<id>")
def foto_usuario(id):
    id = int(id)
    return f"Foto do usuario {id} carregado com sucesso"

@app.route("/postar_foto")
def postar_foto():
    return "Opa, estamos em manutenção", 503

if __name__ == "__main__":
    app.run(debug=True)