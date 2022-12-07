from turtle import Turtle

FONT = ('courier', 20, 'normal')
FONT_2 = ('courier', 30, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.ht()
        self.write(f"Score: {self.score}", move=False, align='center', font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=FONT)

    def gameoverwall(self):
        self.goto(0, 0)
        self.write(f"GAME OVER - WALL", move=False, align='center', font=FONT)
        
    def gameoverself(self):
        self.goto(0, 0)
        self.write(f"GAME OVER - SELF", move=False, align='center', font=FONT)


