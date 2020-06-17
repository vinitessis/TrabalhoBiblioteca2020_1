class Livro():

    def __init__(self, livroid = None, titulo = None, autor = None, isbn = None, pgs = None, quant = None):
        self.livroid = livroid
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.pgs = pgs
        self.quant = quant

class Cliente():

    def __init__ (self, clienteid = None, nome = None, endereco = None, cpf = None):
        self.clienteid - clienteid
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf

class Emprestimo():
    def __init__ (self, emprestimoid = None, livroid = None, clienteid = None):
        self.emprestimoid = emprestimoid
        self.livroid = Livro.livroid
        self.clienteid = Cliente.clienteid

class Devolucao():
    def __init__ (self, devolucaoid = None, emprestimoid = None):
        self.devolucaoid = devolucaoid
        self.emprestimoid = Emprestimo.emprestimoid