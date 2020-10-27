class vehicle:
    """ Base class for al  vehicles """

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color


class car(vehicle):
    """ Car class """

    def __init__(self, name, manufacturer, color, year):
        print('Creating a car')
        super().__init__(name, manufacturer, color)
        self.year = 2017
        self.wheels = 4


if __name__ == "__main__":
    c = car('Mustang 5.0 GT coupe', 'Ford', 'Red', 2017)
    print(c.name, c.year, c.wheels)
