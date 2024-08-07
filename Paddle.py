import turtle
class Paddle:
    def __init__(self, selection, screen):
        if selection == 1:
            self.paddle_image = r"assets/paddle_1.gif"
            screen.register_shape(self.paddle_image)
            self.paddle = turtle.RawTurtle(screen, shape=self.paddle_image, visible=False)
        elif selection == 2:
            self.paddle_image = r"assets/paddle_2.gif"
            screen.register_shape(self.paddle_image)
            self.paddle = turtle.RawTurtle(screen, shape=self.paddle_image, visible=False)
        elif selection == 3:
            self.paddle_image = r"assets/paddle_3.gif"
            screen.register_shape(self.paddle_image)
            self.paddle = turtle.RawTurtle(screen, shape=self.paddle_image, visible=False)
        self.paddle.penup()
        self.paddle.goto(0, -380)
        self.paddle.showturtle()

    def left(self):
        if self.paddle.xcor() > -350:
            self.paddle.bk(35)
    def right(self):
        if self.paddle.xcor() < 350:
            self.paddle.fd(35)