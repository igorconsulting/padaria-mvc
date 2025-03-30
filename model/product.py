import unicodedata
from .entity import Entity

class Product(Entity):
    def __init__(self, name: str, taste: str):
        super().__init__(name)
        self.taste = self.__clean_taste(taste)

    def __clean_name(self, name: str) -> str:
        """
        Cleans the product name by:
        - Removing leading and trailing spaces.
        - Converting all characters to lowercase.
        - Removing accents from characters (e.g., 'Bolo de Morango' → 'bolo de morango').
        - Keeping only one space between words, even if multiple spaces are provided by the user.
        
        Args:
            name (str): The original name of the product.

        Returns:
            str: The cleaned product name in lowercase, without accents, and with normalized spacing.
        """
        # Remove extra spaces and convert to lowercase
        cleaned_name = ' '.join(name.strip().lower().split())
        
        # Remove accents by normalizing to NFKD form and converting to ASCII
        cleaned_name = unicodedata.normalize('NFKD', cleaned_name).encode('ASCII', 'ignore').decode('utf-8')
        return cleaned_name

    def __clean_taste(self, taste: str) -> str:
        """
        Cleans the product taste description by:
        - Removing leading and trailing spaces.
        - Removing accents from characters (e.g., 'Morango' → 'Morango').
        - Keeping only one space between words, even if multiple spaces are provided by the user.
        
        Note: Unlike the product name, the taste is not converted to lowercase or uppercase
        since it might be case-sensitive depending on your requirements.
        
        Args:
            taste (str): The original taste description of the product.

        Returns:
            str: The cleaned taste description with accents removed and normalized spacing.
        """
        # Remove extra spaces
        cleaned_taste = ' '.join(taste.strip().split())
        
        # Remove accents by normalizing to NFKD form and converting to ASCII
        cleaned_taste = unicodedata.normalize('NFKD', cleaned_taste).encode('ASCII', 'ignore').decode('utf-8')
        
        return cleaned_taste

    def __str__(self):
        """
        Returns a string representation of the Product object.
        
        Returns:
            str: A formatted string describing the product.
        """
        return f"Produto {self.name} de {self.taste}"