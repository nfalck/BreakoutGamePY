import turtle
import time
class Ball:
    def __init__(self, selection, screen):
        if selection == 1:
            self.ball_image = r"assets/ball_1.gif"
            screen.register_shape(self.ball_image)
            self.ball = turtle.RawTurtle(screen, shape=self.ball_image, visible=False)
        elif selection == 2:
            self.ball_image = r"assets/ball_2.gif"
            screen.register_shape(self.ball_image)
            self.ball = turtle.RawTurtle(screen, shape=self.ball_image, visible=False)
        elif selection == 3:
            self.ball_image = r"assets/ball_3.gif"
            screen.register_shape(self.ball_image)
            self.ball = turtle.RawTurtle(screen, shape=self.ball_image, visible=False)
        self.ball.penup()
        self.ball.goto(0,-355)
        self.ball.showturtle()
        self.ball_x_move = 10
        self.ball_y_move = 10

    def move(self):
        new_x = self.ball.xcor() + self.ball_x_move
        new_y = self.ball.ycor() + self.ball_y_move
        self.ball.goto(x=new_x, y=new_y)

    def collision_with_walls(self):
        if self.ball.xcor() >= 375:
            self.ball_x_move *= -1
        elif self.ball.xcor() <= -375:
            self.ball_x_move *= -1
        elif self.ball.ycor() >= 375:
            self.ball_y_move *= -1

    def collision_with_paddle(self, paddle, scoreboard):
        if self.ball.ycor() < -375:
            self.ball.hideturtle()
            self.ball.goto(0,-50)
            self.ball.showturtle()
            scoreboard.lives -= 1
            scoreboard.update_score()
        elif self.ball.ycor() < -355:
            if self.ball.xcor() <= paddle.paddle.xcor() + 50 and self.ball.xcor() >= paddle.paddle.xcor() - 50:
                self.ball_y_move *= -1

    def collision_with_bricks(self, bricks, scoreboard):
        for brick in bricks.bricks:
            if self.ball.distance(brick.brick) < 50:
                if (self.ball.xcor() < brick.brick.xcor() + 50 and self.ball.xcor() > brick.brick.xcor() - 50):
                    if self.ball.ycor() < brick.brick.ycor() - 16:
                        self.ball_y_move *= -1
                    elif (self.ball.ycor() < brick.brick.ycor()-16 and self.ball.ycor() > brick.brick.ycor()+16):
                        self.ball_x_move *= -1
                    elif self.ball.ycor() > brick.brick.ycor() + 16:
                        self.ball_y_move *= -1
                    scoreboard.score += 100
                    scoreboard.update_score()
                    brick.brick.clear()
                    brick.brick.hideturtle()
                    bricks.bricks.remove(brick)
                    time.sleep(0.01)