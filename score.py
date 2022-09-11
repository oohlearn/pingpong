from turtle import Turtle
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score_l = 0
        self.score_r = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.score_l}", False, align="center", font=FONT)
        self.goto(100, 200)
        self.write(f"{self.score_r}", False, align="center", font=FONT)

    def get_score(self, player):
        if player == "right":
            self.score_r += 1
            self.update_score_board()
        else:
            self.score_l += 1
            self.update_score_board()




