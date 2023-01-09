from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_scores()
    
    def update_scores(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.left_score, align="center", font=("Comic Sans MS",50, "normal"))
        self.goto(100,200)
        self.write(self.right_score, align="center", font=("Comic Sans MS",50, "normal"))

    def left_goal(self):
        self.left_score+=1
        self.update_scores()
    
    def right_goal(self):
        self.right_score+=1
        self.update_scores()