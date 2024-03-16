import mysql.connector

class Usuario:
    def __init__(self, nomePagador, cpf, valeRef, valeAli, salario):
        self.nomePagador = nomePagador
        self.cpf = cpf
        self.valeRef = valeRef
        self.valeAli = valeAli
        self.salario = salario

class Conta:
    def __init__(self, nomePagador, valorConta, tipoConta, data_pagamento, forma_pagamento, usuario):
        self.nomePagador = nomePagador
        self.valorConta = valorConta
        self.tipoConta = tipoConta
        self.data_pagamento = data_pagamento
        self.forma_pagamento = forma_pagamento
        self.usuario = usuario

def criando_conta(nomePagador, valorConta, tipoConta, data_pagamento, forma_pagamento, usuario):
    """
    Cria uma nova conta para o usuário especificado.

    Args:
        nomePagador: Nome do pagador da conta.
        valorConta: Valor da conta.
        tipoConta: Tipo da conta (ex: "Energia", "Telefone").
        data_pagamento: Data de pagamento da conta.
        forma_pagamento: Forma de pagamento da conta (ex: "Boleto", "Cartão").
        usuario: Objeto da classe Usuario que representa o pagador.

    Returns:
        Objeto da classe Conta criado.
    """

    # Validações e lógica de negócio para criação da conta

    if not nomePagador:
        raise ValueError("Nome do pagador é obrigatório")
    if not valorConta:
        raise ValueError("Valor da conta é obrigatório")
    if not tipoConta:
        raise ValueError("Tipo da conta é obrigatório")
    if not data_pagamento:
        raise ValueError("Data de pagamento é obrigatório")
    if not forma_pagamento:
        raise ValueError("Forma de pagamento é obrigatório")
    if not usuario:
        raise ValueError("Usuário é obrigatório")

    # Verifica se o usuário existe
    conexao = db_connect()
    cursor = conexao.cursor()
    sql_verifica_usuario = """
        SELECT * FROM Usuario WHERE nomePagador = %s
    """
    cursor.execute(sql_verifica_usuario, (nomePagador,))
    usuario_existe = cursor.fetchone()
    cursor.close()
    conexao.close()

    if not usuario_existe:
        raise ValueError(f"Usuário com nome '{nomePagador}' não encontrado.")

    # Conexão com o banco de dados
    conexao = db_connect()

    # Inserindo a nova conta na tabela Conta
    cursor = conexao.cursor()
    sql = """
        INSERT INTO Conta (nomePagador, valorConta, tipoConta, data_pagamento, forma_pagamento, Usuario_nomePagador)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (nomePagador, valorConta, tipoConta, data_pagamento, forma_pagamento, usuario.nomePagador))
    conexao.commit()
    cursor.close()
    conexao.close()

    # Retorna a conta criada
    return Conta(nomePagador, valorConta, tipoConta, data_pagamento, forma_pagamento, usuario)

def criando_usuario(nomePagador, cpf, valeRef, valeAli, salario):
    """
    Cria um novo usuário.

    Args:
        nomePagador: Nome do pagador.
        cpf: CPF do pagador.
        valeRef: Valor do vale-refeição.
        valeAli: Valor do vale-alimentação.
        salario: Salário do pagador.

    Returns:
        Objeto da classe Usuario criado.
    """

    # Validações e lógica de negócio para criação do usuário

    if not nomePagador:
        raise ValueError("Nome do pagador é obrigatório")

    # Conexão com o banco de dados
    conexao = db_connect()

    # Inserindo o novo usuário na tabela Usuario
    cursor = conexao.cursor()
    sql = """
        INSERT INTO Usuario (nomePagador, cpf, valeRef, valeAli, salario)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (nomePagador, cpf, valeRef, valeAli, salario))
    conexao.commit()
    cursor.close()
    conexao.close()

def db_connect():
    """
    Estabelece uma conexão com o banco de dados MySQL.

    Returns:
        Objeto de conexão com o banco de dados.
    """

    # Parâmetros de conexão
    host = "127.0.0.1"
    port = 3306
    database = "mydb"
    user = "root"
    password = "mysqlroot"

    try:
        # Conectando ao banco de dados
        conexao = mysql.connector.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
        )

        return conexao

    except mysql.connector.Error as e:
        # Tratamento de erros de conexão
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def alterando_conta(conta, novo_valorConta, novo_tipoConta, nova_data_pagamento, nova_forma_pagamento):
  """
  Altera os dados de uma conta existente.

  Args:
    conta: Objeto da classe Conta a ser alterada.
    novo_valorConta: Novo valor da conta.
    novo_tipoConta: Novo tipo da conta.
    nova_data_pagamento: Nova data de pagamento da conta.
    nova_forma_pagamento: Nova forma de pagamento da conta.

  Returns:
    Objeto da classe Conta alterado.
  """
  # Validações e lógica de negócio para alteração da conta

  if not conta:
    raise ValueError("Conta não informada")

  # Conexão com o banco de dados
  conexao = db_connect()

  # Atualizando a conta na tabela Conta
  cursor = conexao.cursor()


def alterando_usuario(usuario, novo_cpf, novo_valeRef, novo_valeAli, novo_salario):
  """
  Altera os dados de um usuário existente.

  Args:
    usuario: Objeto da classe Usuario a ser alterado.
    novo_cpf: Novo CPF do usuário.
    novo_valeRef: Novo valor do vale-refeição.
    novo_valeAli: Novo valor do vale-alimentação.
    novo_salario: Novo salário do usuário.

Returns:
    Objeto da classe Usuario alterado.
  """
  # Validações e lógica de negócio para alteração do usuário

  if not usuario:
    raise ValueError("Usuário não informado")

  # Conexão com o banco de dados
  conexao = db_connect()

  # Atualizando o usuário na tabela Usuario
  cursor = conexao.cursor()
  sql = """
    UPDATE Usuario
    SET cpf = %s, valeRef = %s, valeAli = %s, salario = %s
    WHERE nomePagador = %s
  """
  cursor.execute(sql, (novo_cpf, novo_valeRef, novo_valeAli, novo_salario, usuario.nomePagador))
  conexao.commit()
  cursor.close()
  conexao.close()

  # Retorna o usuário alterado
  usuario.cpf = novo_cpf
  usuario.valeRef = novo_valeRef
  usuario.valeAli = novo_valeAli
  usuario.salario = novo_salario
  return usuario



def removendo_conta(conta):
  """
  Remove uma conta existente.

  Args:
    conta: Objeto da classe Conta a ser removida.
  """
  # Validações e lógica de negócio para remoção da conta

  if not conta:
    raise ValueError("Conta não informada")

  # Conexão com o banco de dados
  conexao = db_connect()

  # Removendo a conta da tabela Conta
  cursor = conexao.cursor()
  sql = """
    DELETE FROM Conta
    WHERE nomePagador = %s
  """
  cursor.execute(sql, (conta.nomePagador,))
  conexao.commit()
  cursor.close()
  conexao.close()

def removendo_usuario(usuario):
  """
  Remove um usuário existente.

  Args:
    usuario: Objeto da classe Usuario a ser removido.
  """
  # Validações e lógica de negócio para remoção do usuário

  if not usuario:
    raise ValueError("Usuário não informado")

  # Conexão com o banco de dados
  conexao = db_connect()

  # Removendo o usuário da tabela Usuario
  cursor = conexao.cursor()
  sql = """
    DELETE FROM Usuario
    WHERE nomePagador = %s
  """
  cursor.execute(sql, (usuario.nomePagador,))
  conexao.commit()
  cursor.close()
  conexao.close()




def lista_contas():
  """
  Lista todas as contas cadastradas no sistema.
  """
  contas = busca_todas_contas()
  for conta in contas:
    print(f"{conta.nomePagador} | {conta.valorConta} | {conta.tipoConta} | {conta.data_pagamento} | {conta.forma_pagamento}")

def lista_usuarios():
  """
  Lista todos os usuários cadastrados no sistema.
  """
  usuarios = busca_todos_usuarios()
  for usuario in usuarios:
    print(f"{usuario.nomePagador} | {usuario.cpf} | {usuario.valeRef} | {usuario.valeAli} | {usuario.salario}")



def busca_todas_contas():
  """
  Busca todas as contas cadastradas no banco de dados.

  Returns:
    Lista de objetos da classe Conta.
  """

  conexao = db_connect()
  cursor = conexao.cursor()
  sql = """
    SELECT * FROM Conta
  """
  cursor.execute(sql)
  contas = []
  for row in cursor:
    conta = Conta(
      row[0],
      row[1],
      row[2],
      row[3],
      row[4],
      # Implementar a busca do usuário
      busca_usuario_por_nome(row[5]),
    )
    contas.append(conta)
  cursor.close()
  conexao.close()
  return contas


def busca_todos_usuarios():
  """
  Busca todos os usuários cadastrados no banco de dados.

  Returns:
    Lista de objetos da classe Usuario.
  """

  conexao = db_connect()
  cursor = conexao.cursor()
  sql = """
    SELECT * FROM Usuario
  """
  cursor.execute(sql)
  usuarios = []
  for row in cursor:
    usuario = Usuario(
      row[0],
      row[1],
      row[2],
      row[3],
      row[4],
    )
    usuarios.append(usuario)
  cursor.close()
  conexao.close()
  return usuarios

def busca_usuario_por_nome(nome):
  """
  Busca um usuário no banco de dados pelo seu nome.

  Args:
    nome: O nome do usuário a ser buscado.

  Returns:
    Objeto da classe Usuario se o usuário for encontrado.
    None se o usuário não for encontrado.
  """

  conexao = db_connect()
  cursor = conexao.cursor()
  sql = """
    SELECT * FROM Usuario WHERE nomePagador = %s
  """
  cursor.execute(sql, (nome,))
  usuario = cursor.fetchone()
  cursor.close()
  conexao.close()

  if usuario:
    return Usuario(
      usuario[0],
      usuario[1],
      usuario[2],
      usuario[3],
      usuario[4],
    )
  else:
    return None


def busca_conta_por_nome_pagador(nomePagador):
  """
  Busca uma conta no banco de dados pelo nome do pagador.

  Args:
    nomePagador: O nome do pagador da conta a ser buscada.

  Returns:
    Objeto da classe Conta se a conta for encontrada.
    None se a conta não for encontrada.
  """

  conexao = db_connect()
  cursor = conexao.cursor()
  sql = """
    SELECT * FROM Conta WHERE nomePagador = %s
  """
  cursor.execute(sql, (nomePagador,))
  conta = cursor.fetchone()
  cursor.close()
  conexao.close()

  if conta:
    return Conta(
      conta[0],
      conta[1],
      conta[2],
      conta[3],
      conta[4],
      # Implementar a busca do usuário
      busca_usuario_por_nome(conta[5]),
    )
  else:
    return None