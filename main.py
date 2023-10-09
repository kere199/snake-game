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
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on ==True:
    time.sleep(0.1)
    snake.move()
    screen.update()

   


screen.exitonclick()
