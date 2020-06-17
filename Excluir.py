import mysql.connector

def excluir_livro():
    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")

    result = cursor.fetchall()
    print("=" * 13)
    print("Excluir Livro")
    print("=" * 13)
    
    print("=" * 18)
    print("Livros Cadastrados")
    print("=" * 18)
    for livro in result:
        print(livro)
        print("=" * 50)

    id = input("Informe o id do livro que você quer excluir: ")

    cursor.execute("DELETE FROM livros WHERE livroid= " + id)

    conn.commit()

    print("=" * 27)
    print("Livro Excluído com Sucesso!")
    print("=" * 27)

    cursor.close()
    conn.close()

def excluir_cliente():
    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")

    result = cursor.fetchall()
    print("=" * 15)
    print("Excluir Cliente")
    print("=" * 15)
    
    print("=" * 20)
    print("Clientes Cadastrados")
    print("=" * 20)
    for cliente in result:
        print(cliente)
        print("=" * 70)

    id = input("Informe o id do cliente que você quer excluir: ")

    cursor.execute("DELETE FROM clientes WHERE clienteid= " + id)

    conn.commit()

    print("=" * 29)
    print("Cliente Excluído com Sucesso!")
    print("=" * 29)

    cursor.close()
    conn.close()

