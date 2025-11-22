from dados._conexao_banco import _conectar_banco

def criar_cliente():
    cpf = int(input("Insira o CPF(00099988877): "))
    nome = input("Insira o Nome: ")
    telefone = int(input("Insira o Telefone (55988887777): "))

    conexao = _conectar_banco()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO cliente (cpf, nome, telefone)
                VALUES (%s, %s, %s)
            """, (str(cpf), nome, telefone))
            conexao.commit()
            print("Cliente criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar cliente: {e}")
        finally:
            cursor.close()
            conexao.close()

def buscar_cliente():
    return

def atualizar_cliente():
    return

def deletar_cliente():
    return