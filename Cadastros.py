import mysql.connector
import Classes as classe

def cadastrar_livro():
    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')

    print("=" * 17)
    print("Cadastro de Livro")
    print("=" * 17)

    livro = classe.Livro()

    cursor = conn.cursor()
    query = "INSERT INTO livros (titulo, autor, isbn, pgs, quant) VALUES ("
    query+= " '" + str(livro.get_titulo()) + "' , '" + str(livro.get_autor()) + "' , '" + str(livro.get_isbn()) + "' , '" + str(livro.get_pgs()) + "' , '" + str(livro.get_quant()) + "' )"
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

    cursor = conn.cursor()
    query = "INSERT INTO clientes (nome, endereco, cpf) VALUES ("
    query+= " '" + str(cliente.get_nome()) + "' , '" + str(cliente.get_endereco()) + "' , '" + str(cliente.get_cpf()) + "' )"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

    print("=" * 19)
    print("Cliente cadastrado com sucesso")
    print("=" * 19)