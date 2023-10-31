#Bugatti models
class Model1:
    name = "Parent Model"
    speed = 400
    mass = 2000
    length = 4.5
    width = 2
    height = 1.2
    def __str__(self):
        print(f'Name - {self.name}\n'
                f'Speed - {self.speed}\n'
                f'Mass - {self.mass}\n'
                f'Length - {self.length}\n'
                f'Width - {self.width}\n'
                f'Height - {self.height}\n')

class Model2(Model1):
    name = "veyron"
    speed = 320
    mass = 1980
class Model3(Model2):
    name = "centodieci"
    mass = 2000
class Model4(Model3):
    name = "chiron"
    speed = 500
    mass = 1450
    length = 4.8
    width = 2.3
    height = 1
class Model5(Model4):
    speed = 380
    mass = 1960
    length = 4.6

veyron = Model1()
centodieci = Model2()
chiron = Model3()
bolide = Model4()
divo = Model5()
models = [veyron, centodieci, chiron, bolide, divo]
for model in models:
    model.__str__()