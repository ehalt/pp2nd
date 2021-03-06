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
    def change_gear(self, gear_name):
        """ Method for changing gear """
        print(self.name, 'is changing gear to ', gear_name)


if __name__ == "__main__":
    c = car("Mustang 5.0 GT coupe", "Ford", "Red")
    c.drive()
    c.brake()
    c.change_gear('P')


