import mysql.connector

def pesquisa_livros(descricao):
    idlivros = []
    quant = []
    
    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')
    cursor = conn.cursor()
    query = "SELECT livroid, titulo, autor, quantdisponivel FROM livros WHERE titulo like '%"
    query += str(descricao) + "%' or autor like '%"
    query += str(descricao) + "%'"
    cursor.execute(query)
    result = cursor.fetchall()

    print("=" * 140)
    print("Livros".center(140," "))
    print("=" * 140)
    print("|", "ID".center(8," "), "|", "Título".center(50," "), "|", "Autor".center(50," "), "|", "Quantidade Disponível".center(22," "), "|")
    for livro in result:
        print("|", str(livro[0]).center(8," "), "|", str(livro[1]).center(50," "), "|", str(livro[2]).center(50," "), "|", str(livro[3]).center(22," "), "|")
        idlivros.append(livro[0])
        quant.append(livro[3])
    cursor.close()
    conn.close()
    return idlivros, quant


def pesquisa_clientes(descricao):
    idclientes = []

    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')

    cursor = conn.cursor()
    query = "SELECT clienteid, nome, cpf FROM clientes WHERE nome like '%"
    query += str(descricao) + "%' or cpf like '%"
    query += str(descricao) + "%'"
    cursor.execute(query)
    result = cursor.fetchall()
 
    print("=" * 83)
    print("Livros".center(83," "))
    print("=" * 83)
    print("|", "ID".center(8," "), "|", "Nome".center(50," "), "|", "CPF".center(15," "), "|")
    for livro in result:
        print("|", str(livro[0]).center(8," "), "|", str(livro[1]).center(50," "), "|", str(livro[2]).center(15," "), "|")
        idclientes.append(livro[0])
    cursor.close()
    conn.close()
    return idclientes
