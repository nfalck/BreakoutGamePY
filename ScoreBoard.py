import turtle
class ScoreBoard:
    def __init__(self, screen):
        self.scoreboard = turtle.RawTurtle(screen)
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.color('white')
        self.score = 0
        self.lives = 5
        self.scoreboard.goto(-300, 330)
        self.scoreboard.write(f'Score: {self.score}  Lives: {self.lives}', font=('Lexend', 15, 'normal'))

    def update_score(self):
        self.scoreboard.clear()
        self.scoreboard.write(f'Score: {self.score}  Lives: {self.lives}', font=('Lexend', 15, 'normal'))