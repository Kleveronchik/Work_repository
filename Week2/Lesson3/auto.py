from humanrole import HumanRole
from autotype import AutoType
from human import Human
class Auto:
    def __init__(self, model:str, type:AutoType):
        self.Model:str = model
        self.Type:AutoType = type
        self.Passengers:list = list()
        self.Drivers:list = list()
    def AddPassengers(self, human:Human):
        if(human.Role == HumanRole.PASSENGER):
            self.Passengers.append(human)
    def AddDrivers(self, human:Human):
        if(human.Role == HumanRole.DRIVER):
            self.Drivers.append(human)
    def __str__(self):
        return (f'Passengers:\n {''.join(self.Passengers)}\n'
                f'Drivers:\n {''.join(self.Drivers)}')