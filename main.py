import turtle as t 
from turtle import Screen, Turtle
import time
from snake import Snake

screen = t.Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.update()
screen.setup(width=600, height=600)


positions = [(0,0), (20,0), (40,0)]


snake = Snake()

game_is_on = True
while game_is_on ==True:
    time.sleep(1)
    snake.move()
    screen.update()

   


screen.exitonclick()
