import mysql.connector

def listar_livros():
    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")

    result = cursor.fetchall()

    print("=" * 183)
    print("Relatório de Livros".center(183," "))
    print("=" * 183)
    print("|", "ID".center(8," "), "|", "Título".center(50," "), "|", "Autor".center(50," "), "|", "ISBN".center(15," "), "|", "Número de Páginas".center(20," "), "|", "Quantidade Disponível".center(20," "), "|")
    for livro in result:
        print("|", str(livro[0]).center(8," "), "|", str(livro[1]).center(50," "), "|", str(livro[2]).center(50," "), "|", str(livro[3]).center(15," "), "|", str(livro[4]).center(20," "), "|", str(livro[5]).center(21," "), "|")

    cursor.close()
    conn.close()

def listar_livros():
    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")

    result = cursor.fetchall()

    print("=" * 183)
    print("Relatório de Livros".center(183," "))
    print("=" * 183)
    print("|", "ID".center(8," "), "|", "Título".center(50," "), "|", "Autor".center(50," "), "|", "ISBN".center(15," "), "|", "Número de Páginas".center(20," "), "|", "Quantidade Disponível".center(20," "), "|")
    for livro in result:
        print("|", str(livro[0]).center(8," "), "|", str(livro[1]).center(50," "), "|", str(livro[2]).center(50," "), "|", str(livro[3]).center(15," "), "|", str(livro[4]).center(20," "), "|", str(livro[5]).center(21," "), "|")

    cursor.close()
    conn.close()