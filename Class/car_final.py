class car:
    def __init__(self, n, p, c, d, cc):
        self.name = n
        self.utpadon = p
        self.color = c
        self.date = d
        self.power = cc


    def start(self):
        print('name: ', self.name)
        print('utpadon:', self.utpadon)
        print('color: ', self.color)
        print('date:', self.date)
        print('power:', self.power)
        print('starting the engine')

    def brk(self):
        print('The car is going to break for a while')

    def drive(self):
        print("I'm gonna drive the car ")

    def turn(self):
        print('Car is turning left or right')

    def change_gear(self):
        print('Car is changig gear')



my_car1 = car('corolla','xyz company', 'white', '10Aug, 2012', '18,0239')
my_car1.start()
my_car1.brk()
my_car1.drive()
my_car1.turn()
my_car1.change_gear()
