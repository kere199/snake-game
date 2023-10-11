import turtle as t 
from turtle import Screen, Turtle
import time

up = 90
right = 0
left = 180
down = 270

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
        self.head = self.segments[-1]

    def move(self):
          for i in range(0, len(self.segments)-1):
               current = self.segments[i]
               next_one = self.segments[i + 1]
               xy = next_one.pos()
               current.goto(xy)
          self.head.forward(20)
     
    def up(self):
         if self.head.heading() != down:
              self.head.setheading(up)

    def left(self):
         if self.head.heading() != right:
              self.head.setheading(left)

    def right(self):
         if self.head.heading() != left:
              self.head.setheading(right)

    def down(self):
         if self.head.heading() != up:
              self.head.setheading(down)

    def extend_snake(self):
        tail = self.segments[0]
        newtail = Turtle()
        newtail.penup()
        newtail.shape("square")
        newtail.color("white")
        x = tail.xcor()
        y = tail.ycor()
        newtail.goto(x,y)
        self.segments.insert(0,newtail)

    # def check_colision(self):
    #      tur_cors =[]
    #      for segment in self.segments[:-1]:
    #           cor = (segment.xcor(), segment.ycor())
    #           tur_cors.append(cor)
    #      x = self.head.xcor() 
    #      y = self.head.ycor()
    #      head_cor = (x,y)
    #      if head_cor in tur_cors:
    #         return True

    def check_colision(self):
         for s in self.segments[:-1]:
              if s.pos() == self.head.pos():
                   return True

    

              





           