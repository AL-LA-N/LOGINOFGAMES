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

def atualizar():
    print("\nATUALIZAR")

    if len(cadastros) == 0:
        print("Nenhum cadastro encontrado.")
        return

    consultar()

    try:
        id_usuario = int(input("\nDigite o ID que deseja atualizar: "))

        if id_usuario < 1 or id_usuario > len(cadastros):
            print("ID inválido.")
            return

        usuario = cadastros[id_usuario - 1]

        print("\nDigite os novos dados:")

        usuario["nome"] = input("Novo nome: ")
        usuario["email"] = input("Novo e-mail: ")

        print("\nCadastro atualizado com sucesso!")

    except ValueError:
        print("Digite apenas números no ID.")

def excluir():
    print("\nEXCLUIR")

    if len(cadastros) == 0:
        print("Nenhum cadastro encontrado.")
        return

    consultar()

    try:
        id_usuario = int(input("\nDigite o ID que deseja excluir: "))

        if id_usuario < 1 or id_usuario > len(cadastros):
            print("ID inválido.")
            return

        cadastros.pop(id_usuario - 1)

        print("\nCadastro excluído com sucesso!")

    except ValueError:
        print("Digite apenas números no ID.")


def menu():
    while True:
        print("\nGAME EVOLUTION")
        print("1 - Cadastrar")
        print("2 - Consultar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("5 - Sair")


        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()

        elif opcao == "2":
            consultar()

        elif opcao == "3":
            atualizar()

        elif opcao == "4":
            excluir()

        elif opcao == "5":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida.")


menu()
