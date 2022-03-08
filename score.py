from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 25, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score_data.txt") as data:
            self.high_score = int(data.read())
        self.pu()
        self.color("blue")
        self.goto(0, 250)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score} High score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

