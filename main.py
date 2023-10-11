import turtle as t 
from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import ScoreBoard

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

food = Food()
scoreboard= ScoreBoard()
scoreboard.print_score()

game_is_on = True
while game_is_on ==True:
    time.sleep(0.1)
    snake.move()
    screen.update()
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.food_pos()
        snake.extend_snake()
    if snake.head.ycor() < -300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.xcor() > 300:
        scoreboard.game_over()
        break
    if snake.check_colision() == True:
        scoreboard.game_over()
        break
        




screen.exitonclick()
