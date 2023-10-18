from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.score = 0
        self.high_score = 0       

    def print_score(self):
        self.clear()
        self.goto(-150,250)
        self.write(f"score:{self.score}", align= 'center' , font= ("arial",24,"normal"))


    def increase_score(self):
        self.score += 1
        self.print_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align= 'center' , font= ("arial",24,"normal"))

    def zero_score(self):
        self.score = 0

    
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
    


    def print_high_score(self):
        self.goto(150,250)
        self.write(f"highscore:{self.high_score}", align= 'center' , font= ("arial",24,"normal"))

    
