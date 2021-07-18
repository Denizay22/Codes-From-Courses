from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_highscore()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(x=-5, y=270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center",
                   font=("Courier", 20, "normal"))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center",
                   font=("Courier", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_highscore()
        self.score = 0
        self.update_scoreboard()

    def read_highscore(self):
        with open("game_data.txt", mode="r") as file:
            read_data = file.read()
        if len(read_data) == 0:
            self.high_score = 0
            with open("game_data.txt", mode="w") as file:
                file.write("0")
        else:
            self.high_score = int(read_data)

    def update_highscore(self):
        with open("game_data.txt", mode="w") as file:
            file.write(str(self.high_score))

