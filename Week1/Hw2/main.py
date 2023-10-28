import random
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
        print("Meow!")
        self.Happiness += 1
    def sleep(self):
        print("I'll sleep")
        self.Energy += 5
    def chill(self):
        print("I'll chill")
        self.Happiness += 5
        self.Energy += 5
    def run_around(self):
        print("I'll run around the house")
        self.Happiness += 5
        self.Energy -= 20
    def eat(self):
        print("I'll eat\nYum!")
        self.Happiness += 10
        self.Energy += 5
    def is_alive(self):
        if day < 30:
            if self.Energy < 0:
                self.alive = False
                print("\nI'm too tired :(")
            elif self.Happiness < 0:
                print("\nI'm too sad :'(")
                self.alive = False
        else:
            print("\nI lived for one month! :D")
            self.alive = False
    def live(self, day):
        day = "Day " + str(day + 1) + " of " + self.Name + "'s life."
        print(f"{day:=^50}")
        self.Happiness -= random.randint(10, 15)
        self.meow()
        self.eat()
        live_cube = random.randint(1, 2)
        print("I should do something fun")
        if self.Energy < 25:
            print("I am tired")
            self.sleep()
        else:
            if live_cube == 1:
                self.chill()
            else:
                self.run_around()
        self.day_end()
        self.is_alive()
    def day_end(self):
        print(f"Happiness = {self.Happiness}")
        print(f"Energy = {round(self.Energy, 2)}")
        daily_happiness.append(self.Happiness)
        daily_energy.append(self.Energy)
        if day != 0:
            self.day_h = daily_happiness[day] - daily_happiness[day - 1], 2
            self.day_e = daily_energy[day] - daily_energy[day - 1], 2

        else:
            self.day_h = self.Happiness
            self.day_e = self.Energy
        print(f"Happiness got today: {self.day_h}")
        print(f"Energy earned today: {self.day_e}")

fluffy = Cat("Fluffy", 0, 0)
for day in range(31):
    if fluffy.alive == False:
        break
    fluffy.live(day)