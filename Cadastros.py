import mysql.connector
import Classes as classe

def cadastrar_livro():
    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')

    print("=" * 17)
    print("Cadastro de Livro")
    print("=" * 17)

    livro = classe.Livro()

    livro.titulo = input("Digite o título do livro: ")
    livro.autor = input("Digite o autor do livro: ")
    livro.isbn = int(input("Digite o ISBN (somente números): "))
    livro.pgs = int(input("Digite o número de páginas do livro: "))
    livro.quant = int(input("Digite a quantidade de livros: "))

    cursor = conn.cursor()
    query = "INSERT INTO livros (titulo, autor, isbn, pgs, quant) VALUES ("
    query+= " '" + livro.titulo + "' , '" + livro.autor + "' , '" + str(livro.isbn) + "' , '" + str(livro.pgs) + "' , '" + str(livro.quant) + "' )"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

    print("=" * 28)
    print("Livro cadastrado com sucesso")
    print("=" * 28)

def cadastrar_cliente():
    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')

    print("=" * 19)
    print("Cadastro de Cliente")
    print("=" * 19)

    cliente = classe.Cliente()

    cliente.nome = input("Digite o nome do cliente: ")
    cliente.endereco = input("Digite o endereço do cliente: ")
    cliente.cpf = input("Digite o CPF do cliente(somente números): ")

    cursor = conn.cursor()
    query = "INSERT INTO clientes (nome, endereco, cpf) VALUES ("
    query+= " '" + cliente.nome + "' , '" + cliente.endereco + "' , '" + cliente.cpf + "' )"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

    print("=" * 19)
    print("Cliente cadastrado com sucesso")
    print("=" * 19)