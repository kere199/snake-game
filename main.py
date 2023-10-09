import turtle as t 
from turtle import Screen, Turtle

screen = t.Screen()
screen.bgcolor("black")
# screen.screensize(canvwidth=600, canvheight=600, bg="black")
screen.setup(width=600, height=600)


positions = [(0,0), (20,0), (40,0)]
segments = []
for pos in positions:
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.goto(pos)
    segments.append(new_turtle)


screen.exitonclick()
