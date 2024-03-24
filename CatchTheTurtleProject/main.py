import turtle
import random

screen = turtle.Screen()
screen.bgcolor("Light blue")
screen.title("Catch the Turtle")
FONT = ('Arial', 20, 'normal')
score = 0
game_over = False

#make turtle properities
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]
grid_size = 10

#turtle list
turtle_list = []

#score_turtle
score_turtle = turtle.Turtle()

#countdown_turtle
countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")

    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.penup()
    score_turtle.setpos(0,y)
    score_turtle.write(arg="Score: 0",move=False, align="center", font=FONT)
def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

        #print(x, y) koordinat alma

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)
def setup_turtles():
    for i in x_coordinates:
        for j in y_coordinates:
            make_turtle(i,j)
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)
def countdownd(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("Black")
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.penup()
    countdown_turtle.setpos(0, y -30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdownd(time - 1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)
def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdownd(10)
    turtle.tracer(1)


start_game_up()
turtle.mainloop()