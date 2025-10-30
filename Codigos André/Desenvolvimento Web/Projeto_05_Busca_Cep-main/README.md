# 🌍 Buscador de CEP - Projeto Streamlit

## 📋 Situação do Projeto

**Você foi contratado como desenvolvedor Python** para criar uma aplicação web moderna que permita aos usuários buscar informações de endereços a partir de CEPs e visualizá-los em um mapa interativo. A aplicação deve ser intuitiva, responsiva e seguir as melhores práticas de desenvolvimento.

## 🎯 Objetivo do Projeto

Desenvolver um sistema de consulta de CEP que:
- Busque informações de endereço em tempo real
- Exiba os resultados de forma organizada
- Mostre a localização no mapa
- Tenha uma interface profissional e amigável

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem de programação
- **Streamlit** - Framework para aplicações web
- **Pandas** - Manipulação de dados
- **Requests** - Requisições HTTP para APIs
- **AwesomeAPI** - API de consulta de CEPs brasileiros

## 📁 Estrutura do Projeto

```
buscador-cep/
│
├── app.py                 # Aplicação principal Streamlit
├── BuscarCep.py           # Módulo de busca de CEP
├── requirements.txt       # Dependências do projeto
├── README.md             # Documentação do projeto
└── .gitignore           # Arquivos ignorados pelo Git
```

## ⚙️ Instalação e Configuração

### Pré-requisitos
- Python 3.8 ou superior instalado
- Git para controle de versão
- Conexão com internet para instalação de pacotes

### Passo a Passo para Executar o Projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/buscador-cep.git
   cd buscador-cep
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate    # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**
   ```bash
   streamlit run app.py
   ```

5. **Acesse no navegador**
   - Abra: http://localhost:8501
   - A aplicação estará rodando localmente

## 📋 Dependências do Projeto

Crie o arquivo `requirements.txt`:
```txt
streamlit==1.28.0
pandas==2.0.3
requests==2.31.0
```

Instale com:
```bash
pip install -r requirements.txt
```


## 🎨 Funcionalidades Implementadas

### ✅ Busca de CEP
- Validação de CEP (8 dígitos numéricos)
- Consulta em API externa
- Exibição de endereço completo
- Tratamento de erros robusto

### 🗺️ Mapa Interativo
- Visualização da localização
- Coordenadas convertidas automaticamente
- Integração com Streamlit Maps

### 📱 Interface Responsiva
- Sidebar com navegação
- Layout adaptável
- Mensagens de sucesso/erro
- Design profissional

## 🚀 Como Usar a Aplicação

1. **Inicie a aplicação** com `streamlit run app.py`
2. **Selecione "Buscar CEP"** na sidebar
3. **Digite um CEP** válido (apenas números, ex: 01001000)
4. **Clique em "Buscar"** para consultar
5. **Visualize** o endereço e mapa

## 🧪 Testes Recomendados

Teste com estes CEPs exemplos:
- **01001000** - Praça da Sé, São Paulo/SP
- **22030060** - Copacabana, Rio de Janeiro/RJ
- **40130150** - Comércio, Salvador/BA
- **70002900** - Asa Norte, Brasília/DF



## 👨‍💻 Habilidades Desenvolvidas

Ao completar este projeto, os alunos terão praticado:
- ✅ Desenvolvimento com Streamlit
- ✅ Consumo de APIs REST
- ✅ Manipulação de dados com Pandas
- ✅ Tratamento de erros em Python
- ✅ Criação de interfaces web
- ✅ Versionamento com Git
- ✅ Documentação de projetos

