from view.display_builder import Display

class HomeScreen(Display):
    def __init__(self):
        """
        Initializes the HomeScreen display.
        """
        super().__init__()
        
    def display(self) -> str:
        """
        Displays the home screen menu and gets the user's command.
        
        Returns:
            str: The user's command input.
        """
        message = '''
        Sistema Bakery-Fast

        * Cadastrar Produto - 1
        * Cadastrar Cliente - 2
        * Buscar Cliente por Nome - 3
        * Buscar Cliente por Estado  - 4
        * Buscar Produto por Nome - 5
        * Buscar Produto por Sabor - 6
        * Mostrar Banco de Dados de Clientes - 7
        * Mostrar Banco de Dados de Produtos - 8
        * Sair - 0
        '''

        self.show_message(message)
        command = input("\nInsira o comando:")
        return command
