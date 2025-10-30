# 📋 API de Gerenciamento de Tarefas com Flask

## 🎯 Sobre o Projeto
Você foi contratado para desenvolver uma API para gerenciar uma lista de tarefas (To-Do List) usando Flask. Esta API permite operações completas de CRUD (Create, Read, Update, Delete) através dos métodos HTTP: GET, POST, PUT e DELETE.

## ✨ Funcionalidades
- ✅ **Listar todas as tarefas** (GET /tarefas)
- ✅ **Criar nova tarefa** (POST /tarefas)
- ✅ **Atualizar tarefa existente** (PUT /tarefas/<id>)
- ✅ **Excluir tarefa** (DELETE /tarefas/<id>)
- ✅ **Interface web integrada** para testar a API
- ✅ **Suporte a caracteres especiais** (acentos, ç, etc.)

## 🛠️ Tecnologias Utilizadas
- **Python 3.6+**
- **Flask** - Framework web leve
- **HTML/CSS/JavaScript** - Interface de teste
- **JSON** - Formato de dados

## 📦 Estrutura do Projeto
```
api-tarefas-flask/
│
├── templates/
│   └── teste.html          # Interface web para testar a API
│
├── app.py                  # Aplicação Flask principal
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
```

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.6 ou superior instalado
- Pip (gerenciador de pacotes do Python)

### Passo a Passo
1. **Clone ou baixe o projeto**
   ```bash
   git clone <url-do-repositorio>
   cd api-tarefas-flask
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**
   ```bash
   python app.py
   ```

5. **Acesse a aplicação**
   - API: http://localhost:5000/tarefas
   - Interface web: http://localhost:5000/

## 📋 Endpoints da API

### GET /tarefas
Retorna todas as tarefas cadastradas.

**Exemplo de resposta:**
```json
[
  {
    "id": 1,
    "tarefa": "Estudar Flask",
    "feita": false
  }
]
```

### POST /tarefas
Cria uma nova tarefa.

**Corpo da requisição:**
```json
{
  "tarefa": "Nova tarefa"
}
```

**Exemplo de resposta:**
```json
{
  "id": 2,
  "tarefa": "Nova tarefa",
  "feita": false
}
```

### PUT /tarefas/<id>
Atualiza uma tarefa existente.

**Corpo da requisição:**
```json
{
  "tarefa": "Tarefa atualizada",
  "feita": true
}
```

### DELETE /tarefas/<id>
Remove uma tarefa.

**Exemplo de resposta:**
```json
{
  "mensagem": "Tarefa deletada com sucesso"
}
```

## 🧪 Como Testar a API

### Opção 1: Interface Web
Acesse http://localhost:5000/ para usar a interface web integrada(template) que permite testar todos os endpoints.


### Opção 2: Usando Python
```python
import requests

# Listar tarefas
response = requests.get('http://localhost:5000/tarefas')
print(response.json())

# Criar tarefa
nova_tarefa = {"tarefa": "Aprender APIs REST"}
response = requests.post('http://localhost:5000/tarefas', json=nova_tarefa)
print(response.json())
```

## 🎓 Conceitos Aprendidos
- **APIs RESTful** - Arquitetura para APIs web
- **Métodos HTTP** - GET, POST, PUT, DELETE
- **CRUD** - Create, Read, Update, Delete
- **Flask** - Microframework web em Python
- **JSON** - Formato de troca de dados
- **Frontend-Backend** - Comunicação entre cliente e servidor

## 🔧 Personalização e Extensões
Você pode expandir este projeto com:
- [ ] Adicionar banco de dados (SQLite, PostgreSQL)
- [ ] Adicionar autenticação de usuários
- [ ] Adicionar categorias para tarefas
- [ ] Adicionar datas de criação e conclusão
- [ ] Implementar paginação de resultados

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.




---

**Desenvolvido usando Flask e Python**
