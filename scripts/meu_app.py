# GET, POST, jsonify, flask, requests

# cliente <-> servidor
# api, aplicações web

from scripts.meu_app import Flask

app = Flask(__name__)

@app.route('/') # rota Home
def home():
    return 'Servidor iniciado'

app.run(debug=False, port=5000)