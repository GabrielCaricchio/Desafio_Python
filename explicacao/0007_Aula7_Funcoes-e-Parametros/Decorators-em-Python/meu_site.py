from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Essa é minha HomePage'


app.run()