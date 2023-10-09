import turtle as t 
from turtle import Screen, Turtle
import time

screen = t.Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.update()
screen.setup(width=600, height=600)


positions = [(0,0), (20,0), (40,0)]
segments = []
for pos in positions:
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(pos)
    segments.append(new_turtle)


game_is_on = True
while game_is_on ==True:
    time.sleep(1)
    for segment in segments:
       segment.forward(20)
       screen.update()


   


screen.exitonclick()
