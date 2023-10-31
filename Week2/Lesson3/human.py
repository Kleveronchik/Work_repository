from humanrole import HumanRole
from luggagetype import LuggageType
class Human:
    def __init__(self, name:str, role:HumanRole, luggage:LuggageType):
        self.Name:str = name
        self.Role:HumanRole = role
        self.Luggage:LuggageType = luggage
    def __str__(self):
        return (f"Name - {self.Name}\n"
                f"Role - {self.Role}\n"
                f"Luggage - {self.Luggage}\n")