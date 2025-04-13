import unicodedata
from .entity import Entity
import re

class Product(Entity):
    def __init__(self, name: str, taste: str,price):
        super().__init__(name)
        self.taste = self.__clean_taste(taste)
        if isinstance(price, str):  # Limpar e converter para float se for string
            self.price = self.__clean_price(price)
        elif isinstance(price, float):  # Se já é float, só atribui
            self.price = price
        else:
            raise TypeError("Price must be a string or float.")

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
        cleaned_taste = ' '.join(taste.strip().lower().split())
        
        # Remove accents by normalizing to NFKD form and converting to ASCII
        cleaned_taste = unicodedata.normalize('NFKD', cleaned_taste).encode('ASCII', 'ignore').decode('utf-8')
        
        return cleaned_taste
    
    def __clean_price(self, price: str) -> float:
        """
        Cleans and converts the price to a float. It allows only numbers, commas, and points.
        If a comma is used as the decimal separator, it is replaced by a point.
        
        Args:
            price (str): The raw price input as a string.

        Returns:
            float: The cleaned and converted price.
        
        Raises:
            ValueError: If the resulting price cannot be converted to a float.
        """
        # Remove any character that is not a digit, a point, or a comma
        cleaned_price = re.sub(r'[^0-9.,]', '', price)
        
        # Replace commas with points (to support European notation like '12,99')
        cleaned_price = cleaned_price.replace(',', '.')
        
        try:
            # Convert the cleaned string to a float
            return float(cleaned_price)
        except ValueError:
            raise ValueError(f"Invalid price format: '{price}'")

    def __str__(self):
        """
        Returns a string representation of the Product object.
        
        Returns:
            str: A formatted string describing the product.
        """
        return f"Produto {self.name} de {self.taste}, preço: R${self.price}"