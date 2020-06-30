import Pesquisa as pesquisa
from datetime import date, timedelta

class Livro():

    def __init__(self, livroid = None, titulo = None, autor = None, isbn = None, pgs = None, quant = None):
        self.livroid = livroid
        self.titulo = self.set_titulo()
        self.autor = self.set_autor()
        self.isbn = self.set_isbn()
        self.pgs = self.set_pgs()
        self.quant = self.set_quant()

    def get_livroid(self):
        return self.livroid

    def set_titulo(self):
        titulo = input("Digite o título do livro: ").upper()
        return titulo

    def get_titulo(self):
        return self.titulo

    def set_autor(self):
        autor = input("Digite o autor do livro: ").upper()
        return autor

    def get_autor(self):
        return self.autor
    
    def set_isbn(self):
        while True:
            try:
                isbn = int(input("Digite o ISBN (somente números): "))
                if (isbn > 0) and (isbn < 9999999999999):
                    return isbn
                else:
                    print("=" * 24)
                    print("Número de ISBN inválido!")
                    print("=" * 24)
            except:
                print("=" * 24)
                print("Número de ISBN inválido!")
                print("=" * 24)

    def get_isbn(self):
        return self.isbn

    def set_pgs(self):
        while True:
            try:
                pgs = int(input("Digite o número de páginas do livro: "))
                if (pgs > 0):
                    return pgs
                else:
                    print("=" * 24)
                    print("Número de Páginas inválido!")
                    print("=" * 24)
            except:
                print("=" * 24)
                print("Número de Páginas inválido!")
                print("=" * 24)

    def get_pgs(self):
        return self.pgs

    def set_quant(self):
        while True:
            try:
                quant = int(input("Digite a quantidade de livros: "))
                if (quant > 0):
                    return quant
                else:
                    print("=" * 24)
                    print("Número de Quantidade inválido!")
                    print("=" * 24)
            except:
                print("=" * 24)
                print("Número de Quantidade inválido!")
                print("=" * 24)

    def get_quant(self):
        return self.quant

class Cliente():

    def __init__ (self, clienteid = None, nome = None, endereco = None, cpf = None):
        self.clienteid = clienteid
        self.nome = self.set_nome()
        self.endereco = self.set_endereco()
        self.cpf = self.set_cpf()

    def get_clienteid(self):
        return self.clienteid

    def set_nome(self):
        nome = input("Digite o nome do cliente: ").upper()
        return nome

    def get_nome(self):
        return self.nome

    def set_endereco(self):
        endereco = input("Digite o endereço do cliente: ").upper()
        return endereco

    def get_endereco(self):
        return self.endereco

    def set_cpf(self):
        while True:
            try:
                cpf = input("Digite o CPF do cliente (somente números): ")
                cpfint = int(cpf)
                if len(cpf) == 11:
                    return cpf
                else:
                    print("=" * 24)
                    print("Número de CPF inválido1!")
                    print("=" * 24)
            except:
                print("=" * 24)
                print("Número de CPF inválido!")
                print("=" * 24)

    def get_cpf(self):
        return self.cpf

class Emprestimo():
    def __init__ (self):
        self.__livroid = self.set_livroid()
        self.__clienteid = self.set_clienteid()
        self.__dataEmprestimo = self.set_dataEmprestimo()
        self.__dataDevolucao = self.set_dataDevolucao()

    def get_livroid(self):
        return self.__livroid     
    
    def get_clienteid(self):
        return self.__clienteid     
    
    def get_dataEmprestimo(self):
        return self.__dataEmprestimo     
    
    def get_dataDevolucao(self):
        return self.__dataDevolucao     
    
    def set_livroid(self):
        while True:
            try:
                descricao = input("Digite o nome do livro ou do autor: ").upper()
                idlivros = pesquisa.pesquisa_livros(descricao)
                idlivro = int(input("\n\n\nDigite o ID do livro escolhido: "))
                print(idlivros)
                if idlivro in idlivros:
                    return idlivro
                else:
                    print("Livro não cadastrado!")
            except:
                print("Valor colocado não é um id válido!")

    def set_clienteid(self):
         while True:
            descricao = input("Digite o nome do cliente ou do CPF: ").upper()
            idclientes = pesquisa.pesquisa_clientes(descricao)
            idcliente = int(input("\n\n\nDigite o ID do cliente escolhido: "))
            if idcliente in idclientes:
                return idcliente
            else:
                print("=" * 24)
                print("Cliente não cadastrado!")
                print("=" * 24)
            try:
                pass
            except:
                print("=" * 24)
                print("Valor colocado não é um id válido!")
                print("=" * 24)
    
    def set_dataEmprestimo(self):
        data_atual = date.today()
        return data_atual
    
    def set_dataDevolucao(self):
        data_atual = date.today()
        data = data_atual + timedelta(days = 7)
        return data
    

class Devolucao():
    def __init__ (self, devolucaoid = None, emprestimoid = None):
        self.devolucaoid = devolucaoid
        self.emprestimoid = emprestimoid