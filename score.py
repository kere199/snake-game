from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.score = 0       

    def print_score(self):
        self.clear()
        self.write(f"score:{self.score}", align= 'center' , font= ("arial",24,"normal"))


    def increase_score(self):
        self.score += 1
        self.print_score()

