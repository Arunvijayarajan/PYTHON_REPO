import turtle
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Flower Drawing")
flower_turtle = turtle.Turtle()
flower_turtle.speed(10)
def draw_petal(turtle, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.circle(100, 60)  
        turtle.left(120)        
    turtle.end_fill()
def draw_flower(turtle, num_petals, colors):
    for i in range(num_petals):
        draw_petal(turtle, colors[i % len(colors)])
        turtle.left(360 / num_petals)  
flower_turtle.penup()
flower_turtle.goto(0, -200)
flower_turtle.pendown()
flower_turtle.setheading(60)
petal_colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
draw_flower(flower_turtle, 12, petal_colors)
flower_turtle.hideturtle()
turtle.done()

