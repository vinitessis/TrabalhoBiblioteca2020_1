import mysql.connector
import Classes as classe


def cadastrar_livro():
    print("=" * 17)
    print("Cadastro de Livro")
    print("=" * 17)

    livro = classe.Livro()

    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')
    cursor = conn.cursor()
    query = "INSERT INTO livros (titulo, autor, isbn, pgs, quanttotal, quantdisponivel) VALUES ("
    query+= " '" + str(livro.get_titulo()) + "' , '" + str(livro.get_autor()) + "' , '" + str(livro.get_isbn()) + "' , '" + str(livro.get_pgs()) + "' , '" + str(livro.get_quant()) + "' , '" + str(livro.get_quant()) + "' )"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

    print("=" * 28)
    print("Livro cadastrado com sucesso")
    print("=" * 28)

def cadastrar_cliente():
    print("=" * 19)
    print("Cadastro de Cliente")
    print("=" * 19)

    cliente = classe.Cliente()

    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')
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

def emprestimo():
    print("=" * 19)
    print("Emprestimo de livro")
    print("=" * 19)

    emprestimo = classe.Emprestimo()
    livro = emprestimo.get_livroid()
    if livro == 0:
        return 0

    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')
    cursor = conn.cursor()
   

    query = "INSERT INTO emprestimo (livroid, clienteid, dataEmprestimo, DataDevolucao) VALUES ("
    query+= " '" + str(emprestimo.get_livroid()) + "' , '" + str(emprestimo.get_clienteid()) + "' , '" + str(emprestimo.get_dataEmprestimo()) + "' , '" + str(emprestimo.get_dataDevolucao()) + "' )"
    cursor.execute(query)
    conn.commit()

    query = "UPDATE livros SET quantdisponivel = quantdisponivel - '1'" 
    query+= "WHERE livroid = " + str(emprestimo.get_livroid())
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

    print("=" * 19)
    print("Emprestimo realizado com sucesso")
    print("=" * 19)


def devolucao():
    dev = classe.Devolucao()

    conn = mysql.connector.connect(host = 'localhost', database = 'trab_finalap2', user ='root', password = '')
    cursor = conn.cursor()
   
    multa = dev.get_multa()
    paga = 'S'
    if multa > 0:
        paga = 'N'
        print("\n\n\n\n" + "=" * 19)
        print("O valor da multa foi: {}" .format('R$ ' + f'{multa:.2f}'.replace('.', ',')))
        print("\n\n\n\n" + "=" * 19)
        while True:
            paga = input("O Valor foi pago? [S/N]: ")
            paga = paga.upper()
            if paga == 'S':
                paga = 'S'
                break
            elif paga == 'N':
                break
            else:
                print("\n\n\nDigite apenas [S/N]\n\n\n")

    if paga == 'S':
        query = "INSERT INTO devolucao (emprestimoid, dataEntregue, multa) VALUES ("
        query+= " '" + str(dev.get_emprestimoid()) + "' , '" + str(dev.get_dataEntregue()) + "' , '" + str(dev.get_multa()) + "' )"
        cursor.execute(query)
        conn.commit()

        query = "UPDATE livros SET quantdisponivel = quantdisponivel + '1'" 
        query+= "WHERE livroid = " + str(dev.get_livroid())
        cursor.execute(query)
        conn.commit()

        cursor.close()
        conn.close()

        print("=" * 19)
        print("Devolução concluída")
        print("=" * 19)