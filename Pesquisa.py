import mysql.connector
from datetime import date
from Conexao import Conexao

def pesquisa_livros(descricao):
    idlivros = []
    quant = []
    
    banco = Conexao()
    
    query = "SELECT livroid, titulo, autor, quantdisponivel FROM livros WHERE titulo like '%"
    query += str(descricao) + "%' or autor like '%"
    query += str(descricao) + "%' or isbn like '% "
    query += str(descricao) + "%'"
    result = banco.mostrar(query)
  

    print("=" * 143)
    print("Livros".center(143," "))
    print("=" * 143)
    print("|", "ID".center(8," "), "|", "Título".center(50," "), "|", "Autor".center(50," "), "|", "Quantidade Disponível".center(22," "), "|")
    for livro in result:
        print("|", str(livro[0]).center(8," "), "|", str(livro[1]).center(50," "), "|", str(livro[2]).center(50," "), "|", str(livro[3]).center(22," "), "|")
        idlivros.append(livro[0])
        quant.append(livro[3])
    banco.fechar()
    return idlivros, quant


def pesquisa_clientes(descricao):
    idclientes = []

    banco = Conexao()
    
    query = "SELECT clienteid, nome, cpf FROM clientes WHERE nome like '%"
    query += str(descricao) + "%' or cpf like '%"
    query += str(descricao) + "%'"
    result = banco.mostrar(query)
 
    print("=" * 83)
    print("Clientes".center(83," "))
    print("=" * 83)
    print("|", "ID".center(8," "), "|", "Nome".center(50," "), "|", "CPF".center(15," "), "|")
    for livro in result:
        print("|", str(livro[0]).center(8," "), "|", str(livro[1]).center(50," "), "|", str(livro[2]).center(15," "), "|")
        idclientes.append(livro[0])
    banco.fechar()
    
    return idclientes

def pesquisa_emprestimo(idlivro):
    emprestimosid = []
    dataEntrega = []
    livrosid = []
    banco = Conexao()
    
    res = banco.mostrar("SELECT * FROM devolucao")
    if len(res) == 0:
        query = '''SELECT DISTINCT emp.emprestimoid, liv.livroid, liv.titulo, liv.autor, cli.nome, emp.dataEmprestimo, emp.DataDevolucao 
               FROM emprestimo as emp, livros as liv, clientes as cli
               WHERE cli.clienteid = emp.clienteid and 
                     liv.livroid = emp.livroid and
                     liv.livroid =         
            '''
        query += str(idlivro)
    
    else:
        query = '''SELECT DISTINCT emp.emprestimoid, liv.livroid, liv.titulo, liv.autor, cli.nome, emp.dataEmprestimo, emp.DataDevolucao 
               FROM emprestimo as emp, livros as liv, clientes as cli, devolucao as dev
               WHERE cli.clienteid = emp.clienteid and 
                     liv.livroid = emp.livroid and
                     liv.livroid =         
        '''
        query += str(idlivro)            
        query+= ''' and 
                emp.emprestimoid not in
                        (SELECT dev.emprestimoid from devolucao as dev)
                ORDER BY emp.emprestimoid '''
    
    result = banco.mostrar(query)
    print("=" * 188)
    print("Empréstimos".center(188," "))
    print("=" * 188)
    print("|", "ID".center(7," "), "|", "Título".center(40," "), "|", "Autor".center(36," "), "|", "NOME".center(46," "), "|", "Data do empréstimo".center(20," "), "|", "Data da Devolução".center(20," "), "|")
    for emprestimo in result:
        print("|", str(emprestimo[0]).center(7," "), "|", str(emprestimo[2]).center(40," "), "|", str(emprestimo[3]).center(36," "), "|", str(emprestimo[4]).center(46," "), "|", str(date.strftime(emprestimo[5], '%d/%m/%Y')).center(20," "), "|", str(date.strftime(emprestimo[6], '%d/%m/%Y')).center(20," "), "|")
        emprestimosid.append(emprestimo[0])
        livrosid.append(emprestimo[1])
        dataEntrega.append(emprestimo[6])
    return emprestimosid, livrosid, dataEntrega