import mysql.connector
from datetime import date


def listar_livros():

    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")

    print("=" * 197)
    print("Relatório de Livros".center(197," "))
    print("=" * 197)
    print("|", "ID".center(8," "), "|", "Título".center(50," "), "|", "Autor".center(40," "), "|", "ISBN".center(15," "), "|", "Número de Páginas".center(20," "), "|", "Quantidade Total".center(20," "), "|", "Quantidade Disponível".center(20," "), "|")
    for livro in result:
        print("|", str(livro[0]).center(8," "), "|", str(livro[1]).center(50," "), "|", str(livro[2]).center(40," "), "|", str(livro[3]).center(15," "), "|", str(livro[4]).center(20," "), "|", str(livro[5]).center(20," "), "|", str(livro[6]).center(21," "), "|")

    cursor.close()
    conn.close()

def listar_clientes():
    
    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    result = cursor.fetchall()

    print("=" * 136)
    print("Relatório de Clientes".center(136," "))
    print("=" * 136)
    print("|", "ID".center(8," "), "|", "Nome".center(50," "), "|", "Endereço".center(50," "), "|", "CPF".center(15," "), "|")
    for cliente in result:
        print("|", str(cliente[0]).center(8," "), "|", str(cliente[1]).center(50," "), "|", str(cliente[2]).center(50," "), "|", str(cliente[3]).center(15," "), "|")

    cursor.close()
    conn.close()


def listar_emprestimos():
    
    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')
    cursor = conn.cursor()
    cursor.execute('''SELECT emprestimoid, titulo, autor, nome, dataEmprestimo, DataDevolucao
                      FROM emprestimo, livros, clientes
                      WHERE clientes.clienteid = emprestimo.clienteid and
                            livros.livroid = emprestimo.livroid
                      ORDER BY emprestimoid          
    ''')

    result = cursor.fetchall()
    print("=" * 207)
    print("Relatório de Emprestimos".center(173," "))
    print("=" * 207)
    print("|", "ID".center(8," "), "|", "Título".center(40," "), "|", "Autor".center(40," "), "|", "NOME".center(50," "), "|", "Data do empréstimo".center(20," "), "|", "Data da Devolução".center(20," "), "|")
    for emprestimo in result:
        print("|", str(emprestimo[0]).center(8," "), "|", str(emprestimo[1]).center(40," "), "|", str(emprestimo[2]).center(40," "), "|", str(emprestimo[3]).center(50," "), "|", str(date.strftime(emprestimo[4], '%d/%m/%Y')).center(20," "), "|", str(date.strftime(emprestimo[5], '%d/%m/%Y')).center(20," "), "|")

    cursor.close()
    conn.close()