from control.view_controller import ViewController

if __name__ == "__main__":
    controller = ViewController()
    
    while True:
        command = controller.home_screen.display()
        controller.move_screen(command)