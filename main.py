from .view.home_screen import HomeScreen
from .control.view_controler import ViewHandler

def main():
    # inicia tela
    command = HomeScreen()
    #após comando, vai para outra tela
    new_view = ViewHandler(command)

if __name__=="__main__":
    main()