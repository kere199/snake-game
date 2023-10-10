from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.food_pos()
    
    def food_pos(self):
        self.goto((random.randrange(-290,290),random.randrange(-290,290)))
