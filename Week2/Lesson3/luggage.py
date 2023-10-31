from luggagetype import LuggageType
class Luggage:
    def __init__(self, name:str, type:LuggageType):
        self.Name:str = name
        self.Type:LuggageType = type
    def __str__(self):
        return (f"Owner - {self.Name}\n"
                f"Type - {self.Type}")