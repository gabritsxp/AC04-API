from flask import Flask, jsonify
import json
import requests
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
bancoDeDados = mysql.connector.connect(host="localhost", user="root", password="password", database="db_Alunos")

# Rota para obter os registros da tabela tb_aluno
@app.route('/v1/registros', methods=["GET"])
def obter_registros():
    consulta_sql = "SELECT * FROM tb_aluno"
    cursor = bancoDeDados.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()

    registros = []
    for linha in linhas:
        registro = {
            'name': linha[0],
            'sobrenome': linha[1],
            'turma': linha[2]
        }
        registros.append(registro)

    return jsonify(registros)

# Rota para chamar a API de teste usando o método GET
@app.route('/v1/teste/get', methods=["GET"])
def chamar_api_get():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url)
    return response.json()

# Rota para chamar a API de teste usando o método POST
@app.route('/v1/teste/post', methods=["POST"])
def chamar_api_post():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    enviar = {"userId": 1, "title": "Buy milk", "completed": False}
    response = requests.post(api_url, json=enviar)
    return response.json()

# Rota para chamar a API de teste usando o método DELETE
@app.route('/v1/teste/delete', methods=["DELETE"])
def chamar_api_delete():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.delete(api_url)
    return response.json()

if __name__ == '__main__':
    app.run()
