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
