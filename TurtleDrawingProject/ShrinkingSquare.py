import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("Light green")
turtle_screen.title("Turtle python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.right(90)
        size -=5

shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(110)
shrinkingSquare(90)
shrinkingSquare(70)
shrinkingSquare(50)
shrinkingSquare(30)
shrinkingSquare(10)

turtle.done()