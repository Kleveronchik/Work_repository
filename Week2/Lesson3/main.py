from human import Human
from auto import Auto
from auto import AutoType
from auto import HumanRole

humans = list()
yasin = Human('Yasin', HumanRole.DRIVER)
nikita = Human('Nikita', HumanRole.PASSENGER)
illya = Human('Illya', HumanRole.PASSENGER)
arsenii = Human('Arsenii', HumanRole.PASSENGER)
humans.append(yasin)
humans.append(nikita)
humans.append(illya)
humans.append(arsenii)

bmw = Auto("X6", AutoType.CAR)