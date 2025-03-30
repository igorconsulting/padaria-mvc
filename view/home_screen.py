from display_builder import Display

class HomeScreen(Display):
    def __init__(self)->str:
        self.__clear()

        message = '''
        Sistema Bakery-Fast

        * Cadastrar Produto - 1
        * Cadastrar Client - 2
        * Buscar Client por Nome - 3
        * Buscar Client por Estado  - 4
        * Cadastrar Produto - 5
        * Buscar Produto por Nome - 6
        * Buscar Produto por Sabor - 7
        * Mostrar Banco de Dados de Clientes - 8
        * Mostrar Banco de Dados de Produtos - 9
        * Sair - 0
        '''

        print(message)

        command = input("\n Insira o comando:")

        return command