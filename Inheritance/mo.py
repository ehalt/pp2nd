class vehicle:
    """ Base class for al  vehicles """

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def turn(self, direction):
        print('Turning', self.name, 'to', direction)

class car(vehicle):
    """ Car class """
    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = 2017
        self.wheels = 4

    def change_gear(self, gear_name):
        """ Method of changing gear """
        print(self.name, 'is changing gear to', gear_name)

    def turn(self, direction):
        print(self.name, 'is turning', direction)


if __name__ == "__main__":
    c = car('mustang 5.0 GT coupe', 'Ford', 'Red', 2017)
    v = vehicle('softail delux', 'harley - davidson','blue')
    c.turn('right')
    v.turn('right')