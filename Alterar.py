import mysql.connector
import Classes as classe

def alterar_livro():
    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")

    result = cursor.fetchall()

    print("=" * 17)
    print("Alteração de Livro")
    print("=" * 17)

    print("=" * 18)
    print("Livros Cadastrados")
    print("=" * 18)
    for livro in result:
        print(livro)
        print("=" * 100)

    id = input("Informe o id do livro que você quer alterar: ")

    livro = classe.Livro()

    query = "UPDATE livros SET "
    query += "titulo = '" + str(livro.get_titulo()) + "' , "
    query += "autor = '" + str(livro.get_autor()) + "' , "
    query += "isbn = '" + str(livro.get_isbn()) + "' , "
    query += "pgs = '" + str(livro.get_pgs()) + "' , "
    query += "quant = '" + str(livro.get_quant()) + "' "
    query += "WHERE livroid= " + id
    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()

    print("=" * 28)
    print("Livro Atualizado com sucesso")
    print("=" * 28)

def alterar_cliente():
    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")

    result = cursor.fetchall()

    print("=" * 19)
    print("Alteração de Cliente")
    print("=" * 19)

    print("=" * 20)
    print("Clientes Cadastrados")
    print("=" * 20)
    for cliente in result:
        print(cliente)
        print("=" * 100)

    id = input("Informe o id do cliente que você quer alterar: ")

    cliente = classe.Cliente()

    query = "UPDATE clientes SET "
    query += "nome = '" + str(cliente.get_nome()) + "' , "
    query += "endereco = '" + str(cliente.get_endereco()) + "' , "
    query += "cpf = '" + str(cliente.get_cpf()) + "' "
    query += "WHERE clienteid= " + id
    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()

    print("=" * 30)
    print("Cliente Atualizado com sucesso")
    print("=" * 30)