cadastros = []


def cadastrar():
    print("\nCADASTRAR")

    nome = input("Nome: ")
    email = input("E-mail: ")

    usuario = {
        "nome": nome,
        "email": email
    }

    cadastros.append(usuario)

    print("\nCadastro realizado com sucesso!")
