# Cadastra um usuário pelo terminal e salva seus dados no arquivo dados.json.

import json

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

try:
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        usuarios = json.load(arquivo)
except (FileNotFoundError, json.JSONDecodeError):
    usuarios = []

usuario = {
    "nome": nome,
    "email": email,
    "senha": senha
}

usuarios.append(usuario)

with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

print("Cadastro salvo com sucesso!")
