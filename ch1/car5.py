class car:
    def __init__(self, n, c):
        self.name = n
        self.color = c

    def start(self):
        print('name: ', self.name)
        print('color: ', self.color)
        print('starting the engine')

my_car = car('corolla','white')
car.start(my_car)
