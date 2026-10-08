""" creating the score board class"""
from turtle import Turtle

FONT = ("Courier", 20, "bold")
ALIGN = "center"

class Scoreboard(Turtle):
    """creating the scoreboard class, inherit from Turtle class"""
        # Constructor
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"Snake Game Project High Score\data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """ show the current score"""
        self.clear()
        self.write(arg= f"Score : {self.score} High Score : {self.highscore}" , align= ALIGN, font= FONT)

    def reset(self):
        if self.score > self.highscore:
            with open(r"Snake Game Project High Score\data.txt", mode = "w") as file:
                self.highscore = self.score
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """ method to increase the score """
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     """ game over state """
    #     self.goto(0,0)
    #     self.write(arg= "GAME OVER", align= ALIGN, font= FONT)
