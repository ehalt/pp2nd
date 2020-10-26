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


if __name__ == "__main__":
    v1 = vehicle("Fusion 110 ex", "walton", "black")
    v2 = vehicle("Softail delux", "harley-davidson", "blue")
    v3 = vehicle("Mustang 5.0 GT coupe", "ford", "red")

    v1.drive()
    v2.drive()
    v3.drive()

    v1.turn('left')
    v2.turn('right')

    v1.brake()
    v2.brake()
    v3.brake()
