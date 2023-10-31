from human import Human
from humanrole import HumanRole
from autotype import AutoType
from luggage import Luggage
from luggagetype import LuggageType

class Auto:
    def __init__(self, model:str, type:AutoType):
        self.Model:str = model
        self.Type:AutoType = type
        self.Passengers:list = list()
        self.Drivers:list = list()
        self.Luggage:list = list()
    def AddPassengers(self, human:Human):
        if(human.Role == HumanRole.PASSENGER):
            self.Passengers.append(human)
    def AddDrivers(self, human:Human):
        if(human.Role == HumanRole.DRIVER):
            self.Drivers.append(human)
    def __str__(self):
        drivers: str = ''
        passengers: str = ''
        for driver in self.Drivers:
            drivers += f'\n{driver.__str__()}'
        for passenger in self.Passengers:
            passengers += f'\n{passenger.__str__()}'
        return (f'Passengers: {passengers}\n'
                f'Drivers: {drivers}')