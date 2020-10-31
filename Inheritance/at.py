import turtle


class ajobturtle(turtle.Turtle):
    """ AjobTurtle is a class for new type of turtle """
    pass


if __name__ == "__main__":
    motu = ajobturtle()
    print(type(motu))
    motu.left(30)
    motu.forward(200)

    turtle.done()
