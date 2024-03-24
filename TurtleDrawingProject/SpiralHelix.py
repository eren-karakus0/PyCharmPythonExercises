import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Python turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("yellow")
turtle.speed(0)

turtle_colors = ["red", "green", "blue", "purple", "orange", "pink"]

for i in range(10):

    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.left(i)

turtle.mainloop()
#turtle.done()