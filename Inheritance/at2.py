import turtle


class ajobturtle(turtle.Turtle):
    """ AjobTurtle is a class for new type of turtle """
    def forward(self, pixel):
        super().backward(pixel)

    def backward(self, pixel):
        super().forward(pixel)

    def left(self, angle):
        super().right(angle)

    def right(self, angle):
        print('I wont turn right, because i am ajob')

if __name__ == "__main__":
    motu = ajobturtle()
    motu.left(30)
    motu.forward(200)
    motu.left(45)
    motu.backward(100)
    motu.right(90)
    motu.forward(10)

    jhontu = turtle.Turtle()
    jhontu.shape('turtle')
    jhontu.left(30)
    jhontu.forward(200)
    jhontu.left(45)
    jhontu.backward(100)
    jhontu.right(90)
    jhontu.forward(10)

    turtle.done()
    