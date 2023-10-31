from auto import Human
from auto import Auto
from auto import AutoType
from auto import HumanRole
from auto import Luggage
from auto import LuggageType

humans = list()
yasin = Human('Yasin', HumanRole.DRIVER, LuggageType.NONE)
nikita = Human('Nikita', HumanRole.PASSENGER, LuggageType.NONE)
illya = Human('Illya', HumanRole.PASSENGER, LuggageType.NONE)
arsenii = Human('Arsenii', HumanRole.PASSENGER, LuggageType.SUITCASE)
humans.append(yasin)
humans.append(nikita)
humans.append(illya)
humans.append(arsenii)

bmw = Auto("X6", AutoType.CAR)
for human in humans:
    bmw.AddPassengers(human)
    bmw.AddDrivers(human)
suitcase = Luggage("Arsenii", LuggageType.SUITCASE)
'''
for driver in bmw.Drivers:
    print(driver)
for passenger in bmw.Passengers:
    print(passenger)
'''
print(bmw)
print("Luggage:")
print(suitcase)