class vehicle:
    """ base class for all v ehicle """

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print('Driving', self.manufacturer, self.name)

    def turn(self, direction):
        print('Turning', self.name, 'to', direction)

    def brake(self):
        print(self.name, 'is stopping')

class car(vehicle):
    """ Car class """

    def __init__(self, name, manufracturer, color, year):
        self.name = name
        self.manufacturer = manufracturer
        self.color = color
        self.year = 2017
        self.wheels = 4
        print("A new car has been created . name: ", self.name)
        print('It has', self.wheels, 'wheels')
        print('The car was built in ', self.year)

    def change_gear(self, gear_name):
        """ Method of changing gear """
        print(self.name, 'is changing gear to', gear_name)


if __name__ == "__main__":
    c = car('mustang 5.0 GT coupe', 'Ford', 'red', 2017)

