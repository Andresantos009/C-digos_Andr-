# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


nome = input('Qual é seu nome?')
idade = input('Sua idade:')
email = input('Qual é seu email:')
senha = input('Qual é sua senha:')

print(f''' ------------------------------ 
 ---------- CADASTRO ----------
 ------------------------------ 
 Nome: {nome}
 Idade: {idade}
 Email: {email}
 Senha: {senha}''')

print(f'''USUÁRIO CADASTRADO
      Seja bem vindo(a) {nome}
    Email: {email}''')