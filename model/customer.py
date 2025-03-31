from .entity import Entity
import re
import unicodedata

class Customer(Entity):
    def __init__(self, name: str, phone: str, state: str):
        super().__init__(name)
        self.phone = self.__clean_phone(phone)
        self.state = self.__clean_state(state)

    def __clean_phone(self, phone: str) -> str:
        """
        Cleans the phone number by removing all non-digit characters.
        """
        # Keep only digits
        return re.sub(r'\D', '', phone)

    def __clean_state(self, state: str) -> str:
        """
        Cleans the state name by removing leading and trailing spaces, removing accents,
        converting to uppercase, and keeping only one space between words.
        """
        # Normalize spaces
        cleaned_state = ' '.join(state.strip().split())
        
        # Remove accents
        cleaned_state = unicodedata.normalize('NFKD', cleaned_state).encode('ASCII', 'ignore').decode('utf-8')
        
        # Convert to uppercase
        return cleaned_state.upper()

    def __str__(self):
        """
        Returns a string representation of the Client object.
        """
        return f"Cliente {self.name}\nTelefone: {self.phone}\nEstado: {self.state})"