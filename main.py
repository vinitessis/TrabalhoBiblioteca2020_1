
import Cadastros as cad
import Excluir as exc
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
    [3] - Excluir Livro
    [4] - Cadastrar Cliente
    [5] - Alterar Cliente
    [6] - Excluir Cliente
    [7] - Realizar Empréstimo
    [8] - Realizar Devolução
    [9] - Listar Livros
    [10] - Listar Clientes
    [11] - Listar Empréstimos
    [12] - Listar Devoluções
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
        exc.excluir_livro()
    elif opcao == "4":
        cad.cadastrar_cliente()
    elif opcao == "5":
        alt.alterar_cliente()
    elif opcao == "6":
        exc.excluir_cliente()
    elif opcao == "7":
        cad.emprestimo()
        devolucao()
    elif opcao == "9":
        lis.listar_livros()
    elif opcao == "10":
        lis.listar_clientes()
    elif opcao == "11":
        lis.listar_emprestimos()
    elif opcao == "12":
        listar_devolucoes()
    else:
        print("=" * 24)
        print("Valor inválido!")
        print("=" * 24)