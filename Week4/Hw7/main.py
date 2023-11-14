import random
import logging
from logging import *
from logger import Logger
'''
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w",
                    format="New report:%(asctime)s:%(levelname)s - %(message)s")
'''
logger = Logger(DEBUG, 'logs.log', 'a')
daily_happiness = []
daily_energy = []
class Cat:
    def __init__(self, name: str, happiness: int, energy: int):
        self.Name = name
        self.Happiness = happiness
        self.Energy = energy
        self.alive = True
        self.day_h = 0
        self.day_e = 0
    def meow(self):
        logging.debug("Meow!")
        self.Happiness += 1
    def sleep(self):
        logging.debug("I'll sleep")
        self.Energy += 5
    def chill(self):
        logging.debug("I'll chill")
        self.Happiness += 5
        self.Energy += 5
    def run_around(self):
        logging.debug("I'll run around the house")
        self.Happiness += 5
        self.Energy -= 20
    def eat(self):
        logging.debug("I'll eat")
        logging.debug("Yum!")
        self.Happiness += 10
        self.Energy += 5
    def is_alive(self):
        if day < 30:
            if self.Energy < 0:
                self.alive = False
                logging.critical("I'm too tired :(")
            elif self.Happiness < 0:
                logging.critical("I'm too sad :'(")
                self.alive = False
        else:
            logging.info("I lived for one month! :D")
            self.alive = False
    def live(self, day):
        day = "Day " + str(day + 1) + " of " + self.Name + "'s life."
        logging.info(f"{day:=^50}")
        self.Happiness -= random.randint(10, 15)
        self.meow()
        self.eat()
        live_cube = random.randint(1, 2)
        logging.info("I should do something fun")
        if self.Energy < 25:
            logging.warning("I am tired")
            self.sleep()
        else:
            if live_cube == 1:
                self.chill()
            else:
                self.run_around()
        self.day_end()
        self.is_alive()
    def day_end(self):
        logging.info(f"Happiness = {self.Happiness}")
        logging.info(f"Energy = {round(self.Energy, 2)}")
        daily_happiness.append(self.Happiness)
        daily_energy.append(self.Energy)
        if day != 0:
            self.day_h = daily_happiness[day] - daily_happiness[day - 1]
            self.day_e = daily_energy[day] - daily_energy[day - 1]

        else:
            self.day_h = self.Happiness
            self.day_e = self.Energy
        logging.info(f"Happiness got today: {self.day_h}")
        logging.info(f"Energy earned today: {self.day_e}")
fluffy = Cat("Fluffy", 10, 0)
for day in range(31):
    if fluffy.alive == False:
        break
    fluffy.live(day)