import mysql.connector
import Classes as classe
from Conexao import Conexao

def alterar_livro():
    
    banco = Conexao()
    result = banco.mostrar("SELECT * FROM livros")


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
    while True:
        try:
            quantdisponivel = int(input("Informe a quantidade disponível: "))
        except:
            print("=" * 24)
            print("Valor inválido!")
            print("=" * 24)
        break
        

    query = "UPDATE livros SET "
    query += "titulo = '" + str(livro.get_titulo()) + "' , "
    query += "autor = '" + str(livro.get_autor()) + "' , "
    query += "isbn = '" + str(livro.get_isbn()) + "' , "
    query += "pgs = '" + str(livro.get_pgs()) + "' , "
    query += "quanttotal = '" + str(livro.get_quant()) + "' , "
    query += "quantdisponivel = '" + str(quantdisponivel) + "' "
    query += "WHERE livroid= " + id
    banco.executar(query)

    banco.fechar()

    print("=" * 28)
    print("Livro Atualizado com sucesso")
    print("=" * 28)

def alterar_cliente():
    
    banco = Conexao()
    result = banco.mostrar("SELECT * FROM clientes")


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
    banco.executar(query)
    banco.fechar()

    print("=" * 30)
    print("Cliente Atualizado com sucesso")
    print("=" * 30)