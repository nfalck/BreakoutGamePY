import turtle


class ScoreBoard:
    def __init__(self, screen):
        """ Create a turtle that will write the score and lives """
        # Turtle is created and its settings are set
        self.scoreboard = turtle.RawTurtle(screen)
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.color('white')
        # Game is initialized with 0 in score and 5 in lives
        self.score = 0
        self.lives = 5
        self.scoreboard.goto(-350, 330)
        self.scoreboard.write(f'Score: {self.score}  Lives: {self.lives}', font=('Lexend', 15, 'normal'))

    def update_scoreboard(self):
        """ Scoreboard will clear and write new score or lives """
        self.scoreboard.clear()
        self.scoreboard.write(f'Score: {self.score}  Lives: {self.lives}', font=('Lexend', 15, 'normal'))
