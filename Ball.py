import turtle
import time


class Ball:
    def __init__(self, selection, screen):
        """ Create Ball turtle """
        # Ball appearance changes depending on selection of level
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
        # Goes to starting position
        self.ball.penup()
        self.ball.goto(0, -355)
        self.ball.showturtle()
        # The ball's movement speed
        self.ball_x_move = 10
        self.ball_y_move = 10

    def move(self):
        """ Activate movement of the ball """
        # The ball moves by updating its x- and y-coordinates with its movement speed
        new_x = self.ball.xcor() + self.ball_x_move
        new_y = self.ball.ycor() + self.ball_y_move
        self.ball.goto(x=new_x, y=new_y)

    def collision_with_walls(self):
        """ Check the ball's collision with walls """
        # Right wall
        if self.ball.xcor() >= 375:
            self.ball_x_move *= -1
        # Left wall
        elif self.ball.xcor() <= -375:
            self.ball_x_move *= -1
        # Top wall
        elif self.ball.ycor() >= 375:
            self.ball_y_move *= -1

    def collision_with_paddle(self, paddle, scoreboard):
        """ Check the ball's collision with the paddle """
        # If the ball collides with bottom wall, one life is lost, and it starts again in the middle
        if self.ball.ycor() < -375:  # the y-area below bottom wall
            self.ball.hideturtle()
            self.ball.goto(0, -125)
            self.ball.showturtle()
            scoreboard.lives -= 1
            scoreboard.update_scoreboard()
        # If the ball collides with the paddle, it bounces
        elif self.ball.ycor() < -355:  # the y-area below top of paddle
            if paddle.paddle.xcor()-50 <= self.ball.xcor() <= paddle.paddle.xcor() + 50:
                self.ball_y_move *= -1

    def collision_with_bricks(self, bricks, scoreboard):
        """ Check the ball's collision with bricks """
        # Checks every brick that is left
        for brick in bricks.bricks:
            if self.ball.distance(brick.brick) < 50:  # If ball is less than 50px away from middle of brick
                if brick.brick.xcor() - 50 < self.ball.xcor() < brick.brick.xcor() + 50:  # the x-area of the brick
                    if self.ball.ycor() < brick.brick.ycor() - 16:
                        # if it touches the bottom of the brick, it bounces down
                        self.ball_y_move *= -1
                    elif brick.brick.ycor()+16 < self.ball.ycor() < brick.brick.ycor()-16:  # the y-area of the brick
                        self.ball_x_move *= -1
                    elif self.ball.ycor() > brick.brick.ycor() + 16:
                        # if it touches the top of the brick, it bounces up
                        self.ball_y_move *= -1
                    # Update score with 100 for every brick collided
                    scoreboard.score += 100
                    scoreboard.update_scoreboard()
                    # Remove the affected bricks
                    brick.brick.clear()
                    brick.brick.hideturtle()
                    bricks.bricks.remove(brick)
                    # Delay to try to prevent the ball from flying through bricks and getting them all without bouncing
                    time.sleep(0.01)
