import re
from abc import ABC, abstractmethod
import unicodedata

class Entity:
    def __init__(self,name:str):

        self.name = self.__clean_name(name)

    def __clean_name(self, name)->str:
        """
        Cleans the name by:
        - Removing leading and trailing spaces.
        - Converting all characters to lowercase.
        - Removing accents from characters.
        - Keeping only one space between words.
        
        Args:
            name (str): The original name of the entity.

        Returns:
            str: The cleaned name in lowercase, without accents, and with normalized spacing.
        """
        cleaned_name = ' '.join(name.strip().lower().split())
        cleaned_name = cleaned_name = unicodedata.normalize('NFKD', cleaned_name).encode('ASCII', 'ignore').decode('utf-8')

        return cleaned_name

    @abstractmethod
    def __str__(self):
        pass