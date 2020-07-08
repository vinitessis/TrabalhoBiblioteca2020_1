
import Cadastros as cad
import Listar as lis
import Alterar as alt

while True:
    print('''
    ========================================
    MENU
    ========================================
    [0] - Finalizar
    [1] - Cadastrar Livro
    [2] - Alterar Livro
    [3] - Cadastrar Cliente
    [4] - Alterar Cliente
    [5] - Realizar Empréstimo
    [6] - Realizar Devolução
    [7] - Listar Livros
    [8] - Listar Clientes
    [9] - Listar Empréstimos
    [10] - Listar Devoluções
    ========================================''')
    opcao = input('Escolha: ')
    if opcao == "0":
        print("Finalizando...")
        print("Operações Finalizadas!")
        break
    elif opcao == "1":
        cad.cadastrar_livro()
    elif opcao == "2":
        alt.alterar_livro()
    elif opcao == "3":
        cad.cadastrar_cliente()
    elif opcao == "4":
        alt.alterar_cliente()
    elif opcao == "5":
        cad.emprestimo()
    elif opcao == "6":
        cad.devolucao()
    elif opcao == "7":
        lis.listar_livros()
    elif opcao == "8":
        lis.listar_clientes()
    elif opcao == "9":
        lis.listar_emprestimos()
    elif opcao == "10":
        lis.listar_devolucoes()
    else:
        print("=" * 24)
        print("Valor inválido!")
        print("=" * 24)