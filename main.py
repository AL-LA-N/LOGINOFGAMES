def menu_usuario(usuario):
    while True:
        limpar_tela()

        print("=" * 50)
        print(f"              GAME EVOLUTION")
        print("=" * 50)
        print()
        print(f" Usuário: {usuario['nome']}")
        print()
        print(" [ 1 ] PERFIL")
        print(" [ 2 ] BIBLIOTECA")
        print(" [ 3 ] CONFIGURAÇÕES")
        print(" [ 4 ] SAIR DA CONTA")
        print()
        print("=" * 50)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            perfil(usuario)

        elif opcao == "2":
            biblioteca(usuario)

        elif opcao == "3":
            configuracoes(usuario)

        elif opcao == "4":
            print("\nSaindo da conta...")
            break

        else:
            print("\nOpção inválida!")
            pausa()
