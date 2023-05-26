from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/lista', methods=['GET'])
def get():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    lista = response.json()
    return jsonify(lista)


@app.route('/lista/enviar', methods=['POST'])
def create():
    enviar = request.json
    return jsonify(enviar), 201

@app.route('/lista/<int:todo_id>', methods=['DELETE'])
def delete(todo_id):
    return jsonify({'messagem': ' deletado da lista'})

if __name__ == '__main__':
    app.run(port=5000)
