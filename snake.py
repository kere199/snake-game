import turtle as t 
from turtle import Screen, Turtle
import time


positions = [(0,0), (20,0), (40,0)]
class Snake:
    def __init__(self):
        self.segments = []
        for pos in positions:
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(pos)
            self.segments.append(new_turtle)

    def move(self):
          for i in range(0, len(self.segments)-1):
               current = self.segments[i]
               next_one = self.segments[i + 1]
               xy = next_one.pos()
               current.goto(xy)
          self.segments[-1].forward(20)

           