import cadastro


def limpar_tela():
    print("\n" * 3)


def pausa():
    input("\nPressione ENTER para continuar...")


def tela_inicial():
    while True:
        limpar_tela()

        print("=" * 50)
        print("              GAME EVOLUTION")
        print("=" * 50)
        print()
        print("              [ 1 ] ENTRAR")
        print("              [ 2 ] CRIAR CONTA")
        print("              [ 3 ] SAIR")
        print()
        print("=" * 50)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = cadastro.login()

            if usuario:
                menu_usuario(usuario)

        elif opcao == "2":
            cadastro.cadastrar()

        elif opcao == "3":
            print("\nObrigado por jogar!")
            break

        else:
            print("\nOpção inválida!")
            pausa()
