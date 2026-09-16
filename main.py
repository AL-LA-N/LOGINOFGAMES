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


def perfil(usuario):
    limpar_tela()

    print("=" * 50)
    print("                    PERFIL")
    print("=" * 50)

    print()
    print(f"Nome:  {usuario['nome']}")
    print(f"E-mail: {usuario['email']}")
    print(f"ID:    {usuario['id']}")

    print()
    print("=" * 50)

    pausa()


def biblioteca(usuario):
    limpar_tela()

    print("=" * 50)
    print("                 BIBLIOTECA")
    print("=" * 50)

    jogos = usuario.get("jogos", [])

    if not jogos:
        print("\nSua biblioteca está vazia.")
        print("Adicione alguns jogos futuramente!")

    else:
        print()

        for jogo in jogos:
            print(f" - {jogo}")

    print()
    print("=" * 50)

    pausa()


def configuracoes(usuario):
    while True:
        limpar_tela()

        print("=" * 50)
        print("               CONFIGURAÇÕES")
        print("=" * 50)

        print()
        print(" [ 1 ] Alterar nome")
        print(" [ 2 ] Alterar e-mail")
        print(" [ 3 ] Alterar senha")
        print(" [ 4 ] Voltar")
        print()
        print("=" * 50)

        opcao = input("Escolha: ")

        if opcao == "1":
            novo_nome = input("\nNovo nome: ")

            if novo_nome.strip():
                usuario["nome"] = novo_nome
                cadastro.salvar_dados()
                print("\nNome alterado com sucesso!")
            else:
                print("\nNome inválido.")

            pausa()

        elif opcao == "2":
            novo_email = input("\nNovo e-mail: ")

            if cadastro.email_disponivel(novo_email, usuario["id"]):
                usuario["email"] = novo_email
                cadastro.salvar_dados()
                print("\nE-mail alterado com sucesso!")
            else:
                print("\nEsse e-mail já está sendo usado.")

            pausa()

        elif opcao == "3":
            nova_senha = input("\nNova senha: ")

            if len(nova_senha) >= 4:
                usuario["senha"] = nova_senha
                cadastro.salvar_dados()
                print("\nSenha alterada com sucesso!")
            else:
                print("\nA senha precisa ter pelo menos 4 caracteres.")

            pausa()

        elif opcao == "4":
            break

        else:
            print("\nOpção inválida!")
            pausa()


if __name__ == "__main__":
    tela_inicial()
