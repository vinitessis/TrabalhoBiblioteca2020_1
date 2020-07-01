import mysql.connector
from Conexao import Conexao

def excluir_livro():
    
    banco = Conexao()
    result = banco.mostrar("SELECT * FROM livros")

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

    banco.executar("DELETE FROM livros WHERE livroid= " + id)

    print("=" * 27)
    print("Livro Excluído com Sucesso!")
    print("=" * 27)

    banco.fechar()

def excluir_cliente():
    
    banco = Conexao()

    result =banco.mostrar("SELECT * FROM clientes")

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

    banco.executar("DELETE FROM clientes WHERE clienteid= " + id)

    print("=" * 29)
    print("Cliente Excluído com Sucesso!")
    print("=" * 29)

    banco.fechar()

