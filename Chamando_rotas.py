from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/lista', methods=['GET'])
def get():
    response = requests.get('http://localhost:5000/lista')
    lista = response.json()
    return jsonify(lista)

@app.route('/lista/enviar', methods=['POST'])
def create():
    enviar = {'title': 'New Todo', 'completed': False}
    response = requests.post('http://localhost:5000/lista/enviar', json=enviar)
    criando = response.json()
    return jsonify(criando), 201

@app.route('/lista/<int:lista_id>', methods=['DELETE'])
def delete(lista_id):
    url = f'http://localhost:5000/lista/{lista_id}'
    response = requests.delete(url)
    return jsonify({'messagem': ' deletado da lista'})

if __name__ == '__main__':
    app.run(port=5001)
