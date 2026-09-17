# Consulta no dados.json um usuário cadastrado utilizando seu endereço de email.

import json

email = input("Digite o email que deseja consultar: ")

try:
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        usuarios = json.load(arquivo)

    encontrado = False

    for usuario in usuarios:
        if usuario["email"] == email:
            print("\nUsuário encontrado!")
            print("Nome:", usuario["nome"])
            print("Email:", usuario["email"])
            encontrado = True
            break

    if not encontrado:
        print("Usuário não encontrado.")

except (FileNotFoundError, json.JSONDecodeError):
    print("Nenhum usuário cadastrado.")
