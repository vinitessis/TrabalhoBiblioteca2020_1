import mysql.connector
from datetime import date


def listar_livros():

    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    result = cursor.fetchall()
    print("=" * 188)
    print("Relatório de Livros".center(188," "))
    print("=" * 188)
    print("|", "ID".center(7," "), "|", "Título".center(46," "), "|", "Autor".center(36," "), "|", "ISBN".center(15," "), "|", "Número de Páginas".center(20," "), "|", "Quantidade Total".center(20," "), "|", "Quantidade Disponível".center(20," "), "|")
    for livro in result:
        print("|", str(livro[0]).center(7," "), "|", str(livro[1]).center(46," "), "|", str(livro[2]).center(36," "), "|", str(livro[3]).center(15," "), "|", str(livro[4]).center(20," "), "|", str(livro[5]).center(20," "), "|", str(livro[6]).center(21," "), "|")

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
    print("=" * 188)
    print("Relatório de Emprestimos".center(188," "))
    print("=" * 188)
    print("|", "ID".center(8," "), "|", "Título".center(40," "), "|", "Autor".center(40," "), "|", "NOME".center(40," "), "|", "Data do empréstimo".center(20," "), "|", "Data da Devolução".center(20," "), "|")
    for emprestimo in result:
        print("|", str(emprestimo[0]).center(8," "), "|", str(emprestimo[1]).center(40," "), "|", str(emprestimo[2]).center(40," "), "|", str(emprestimo[3]).center(40," "), "|", str(date.strftime(emprestimo[4], '%d/%m/%Y')).center(20," "), "|", str(date.strftime(emprestimo[5], '%d/%m/%Y')).center(20," "), "|")

    
    cursor.close()
    conn.close()


def listar_devolucoes():
    
    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')
    cursor = conn.cursor()
    cursor.execute('''SELECT dev.devolucaoid, liv.titulo, liv.autor, cli.nome, emp.dataEmprestimo, emp.DataDevolucao, dev.dataEntregue, multa
                      FROM emprestimo as emp, livros as liv, clientes as cli, devolucao as dev
                      WHERE cli.clienteid = emp.clienteid and
                            liv.livroid = emp.livroid and
                            emp.emprestimoid = dev.emprestimoid
                      ORDER BY dev.devolucaoid          
    ''')

    result = cursor.fetchall()
    print("=" * 188)
    print("Relatório de Devoluções".center(188," "))
    print("=" * 188)
    print("|", "ID".center(8," "), "|", "Título".center(36," "), "|", "Autor".center(20," "), "|", "NOME".center(36," "), "|", "Data do empréstimo".center(20," "), "|", "Data da Devolução".center(20," "), "|", "Data entregue".center(13, " "), "|", "Multa". center(10, " "), "|")
    for devolucao in result:
        print("|", str(devolucao[0]).center(8," "), "|", str(devolucao[1]).center(36," "), "|", str(devolucao[2]).center(20," "), "|", str(devolucao[3]).center(36," "), "|", str(date.strftime(devolucao[4], '%d/%m/%Y')).center(20," "), "|", str(date.strftime(devolucao[5], '%d/%m/%Y')).center(20," "), "|", str(date.strftime(devolucao[6], '%d/%m/%Y')).center(13," "), "|", str('R$ ' + f'{devolucao[7]:.2f}'.replace('.', ',')).center(10," "), "|")

    cursor.close()
    conn.close()