import classes as cl

def main():
    """
    Função principal que apresenta o painel de controle e permite a escolha de opções.
    """

    while True:
        # Exibindo o menu de opções
        print("\n--- Painel de Controle ---")
        print("1. Criar Conta")
        print("2. Criar Usuário")
        print("3. Alterar Conta")
        print("4. Alterar Usuário")
        print("5. Remover Conta")
        print("6. Remover Usuário")
        print("7. Ver Contas Pagas")
        print("8. Ver Usuários Cadastrados")
        print("0. Sair")

        # Lendo a opção do usuário
        opcao = int(input("Digite a opção desejada: "))

        # Chamando a função específica para a opção escolhida
        if opcao == 1:
            nomePagador = input("Nome do pagador: ")
            valorConta = float(input("Valor da conta: "))
            tipoConta = input("Tipo da conta: ")
            data_pagamento = input("Data de pagamento: ")
            forma_pagamento = input("Forma de pagamento: ")

            try:
                usuario = cl.busca_usuario_por_nome(nomePagador)
                if not usuario:
                    raise ValueError(f"Usuário com nome '{nomePagador}' não encontrado.")
                conta = cl.criando_conta(nomePagador, valorConta, tipoConta, data_pagamento, forma_pagamento, usuario)
                print(f"Conta criada com sucesso: {conta}")
            except ValueError as e:
                print(f"Erro ao criar conta: {e}")

        elif opcao == 2:
            nomePagador = input("Nome do pagador: ")
            cpf = input("CPF: ")
            valeRef = int(input("Valor do vale-refeição: "))
            valeAli = int(input("Valor do vale-alimentação: "))
            salario = int(input("Salário: "))

            try:
                usuario = cl.criando_usuario(nomePagador, cpf, valeRef, valeAli, salario)
                print(f"Usuário criado com sucesso: {usuario}")
            except ValueError as e:
                print(f"Erro ao criar usuário: {e}")

        elif opcao == 3:
            nomePagador = input("Nome do pagador da conta a ser alterada: ")
            novo_valorConta = float(input("Novo valor da conta: "))
            novo_tipoConta = input("Novo tipo da conta: ")
            nova_data_pagamento = input("Nova data de pagamento: ")
            nova_forma_pagamento = input("Nova forma de pagamento: ")

            try:
                conta = cl.busca_conta_por_nome_pagador(nomePagador)
                if not conta:
                    raise ValueError(f"Conta com nome do pagador '{nomePagador}' não encontrada.")
                cl.alterando_conta(conta, novo_valorConta, novo_tipoConta, nova_data_pagamento, nova_forma_pagamento)
                print(f"Conta alterada com sucesso: {conta}")
            except ValueError as e:
                print(f"Erro ao alterar conta: {e}")

        elif opcao == 4:
            nomePagador = input("Nome do usuário a ser alterado: ")
            novo_cpf = input("Novo CPF: ")
            novo_valeRef = int(input("Novo valor do vale-refeição: "))
            novo_valeAli = int(input("Novo valor do vale-alimentação: "))
            novo_salario = int(input("Novo salário: "))

            try:
                usuario = cl.busca_usuario_por_nome(nomePagador)
                if not usuario:
                    raise ValueError(f"Usuário com nome '{nomePagador}' não encontrado.")
                cl.alterando_usuario(usuario, novo_cpf, novo_valeRef, novo_valeAli, novo_salario)
                print(f"Usuário alterado com sucesso: {usuario}")
            except ValueError as e:
                print(f"Erro ao alterar usuário: {e}")

        elif opcao == 5:
            nomePagador = input("Nome do pagador da conta a ser removida: ")

            try:
                conta = cl.busca_conta_por_nome_pagador(nomePagador)
                if not conta:
                    raise ValueError(f"Conta com nome do pagador '{nomePagador}' não encontrada.")
                cl.removendo_conta(conta)
                print(f"Conta removida com sucesso: {conta}")
            except ValueError as e:
                print(f"Erro ao remover conta: {e}")

        elif opcao == 6:
            nomePagador = input("Nome do usuário a ser removido: ")

            try:
                usuario = cl.busca_usuario_por_nome(nomePagador)
                if not usuario:
                    raise ValueError(f"Usuário com nome '{nomePagador}' não encontrado.")
                cl.removendo_usuario(usuario)
                print(f"Usuário removido com sucesso: {usuario}")
            except ValueError as e:
                print(f"Erro ao remover usuário: {e}")

        elif opcao == 7:
            cl.lista_contas()

        elif opcao == 8:
            cl.lista_usuarios()

        elif opcao == 0:
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
