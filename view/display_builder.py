import os
from abc import ABC, abstractmethod

class Display(ABC):
    def __init__(self):
        """
        Initializes the Display by clearing the console.
        """
        self.__clear()

    def __clear(self):
        """
        Clears the console screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_message(self, message: str):
        """
        Displays a message to the user.
        
        Args:
            message (str): The message to be displayed.
        """
        print(f"\n{message}\n")

    @abstractmethod
    def display(self):
        """
        Abstract method to force all subclasses to implement their own display logic.
        """
        pass
