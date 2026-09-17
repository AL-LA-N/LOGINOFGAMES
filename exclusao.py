# Localiza um usuário pelo email, remove seu cadastro e atualiza o dados.json.

import json

email = input("Digite o email do usuário que deseja excluir: ")

try:
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        usuarios = json.load(arquivo)

    usuario_encontrado = None

    for usuario in usuarios:
        if usuario["email"] == email:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        usuarios.remove(usuario_encontrado)

        with open("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

        print("Usuário excluído com sucesso!")
    else:
        print("Usuário não encontrado.")

except (FileNotFoundError, json.JSONDecodeError):
    print("Nenhum usuário cadastrado.")
