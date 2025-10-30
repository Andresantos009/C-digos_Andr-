from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Configurar para caracteres especiais (acentos)
app.config['JSON_AS_ASCII'] = False

# Lista de tarefas (nosso "banco de dados" simulado)
tarefas = [
    {"id": 1, "tarefa": "Estudar Flask", "feita": False},
    {"id": 2, "tarefa": "Fazer exercícios de programação", "feita": True},
    {"id": 3, "tarefa": "Aprender sobre APIs RESTful", "feita": False}
]

# Rota principal - página de teste
@app.route('/')
def index():
    return render_template('teste.html')


# Rota alternativa para a página de teste
@app.route('/teste')
def pagina_teste():
    return render_template('teste.html')


# API - GET: Obter todas as tarefas
@app.route('/tarefas', methods=['GET'])
def obter_tarefas():
    return jsonify(tarefas)


# API - POST: Criar nova tarefa
@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "tarefa": request.json['tarefa'],
        "feita": False
    }
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201


# API - PUT: Atualizar tarefa existente
@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['tarefa'] = request.json.get('tarefa', tarefa['tarefa'])
            tarefa['feita'] = request.json.get('feita', tarefa['feita'])
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404


# API - DELETE: Remover tarefa
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    for index, tarefa in enumerate(tarefas):
        if tarefa['id'] == id:
            del tarefas[index]
            return jsonify({"mensagem": "Tarefa deletada com sucesso"})
    return jsonify({"erro": "Tarefa não encontrada"}), 404




if __name__ == '__main__':
    app.run(debug=True)