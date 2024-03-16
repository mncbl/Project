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