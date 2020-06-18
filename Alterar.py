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

    livro.titulo = input("Digite o título do livro: ")
    livro.autor = input("Digite o autor do livro: ")
    livro.isbn = int(input("Digite o ISBN (somente números): "))
    livro.pgs = int(input("Digite o número de páginas do livro: "))
    livro.quant = int(input("Digite a quantidade de livros: "))

    query = "UPDATE livros SET "
    query += "titulo = '" + str(livro.titulo) + "' , "
    query += "autor = '" + str(livro.autor) + "' , "
    query += "isbn = '" + str(livro.isbn) + "' , "
    query += "pgs = '" + str(livro.pgs) + "' "
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

    cliente.nome = input("Digite o nome do cliente: ")
    cliente.endereco = input("Digite o endereço do cliente: ")
    cliente.cpf = input("Digite o CPF do cliente (somente números): ")

    query = "UPDATE clientes SET "
    query += "nome = '" + str(cliente.nome) + "' , "
    query += "endereco = '" + str(cliente.endereco) + "' , "
    query += "cpf = '" + str(cliente.cpf) + "' "
    query += "WHERE clienteid= " + id
    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()

    print("=" * 30)
    print("Cliente Atualizado com sucesso")
    print("=" * 30)