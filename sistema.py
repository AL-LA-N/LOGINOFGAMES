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


def consultar():
    print("\nCONSULTAR")

    if len(cadastros) == 0:
        print("Nenhum cadastro encontrado.")
        return

    for i, usuario in enumerate(cadastros, start=1):
        print(f"\nID: {i}")
        print(f"Nome: {usuario['nome']}")
        print(f"E-mail: {usuario['email']}")
