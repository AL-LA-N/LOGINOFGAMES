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
