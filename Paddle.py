import turtle


class Paddle:
    def __init__(self, selection, screen):
        """ Create Paddle turtle """
        # Paddle's appearance changes depending on selection of level
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
        # Paddle goes to its starting position
        self.paddle.penup()
        self.paddle.goto(0, -380)
        self.paddle.showturtle()

    def left(self):
        """ Activate paddle's left movement """
        if self.paddle.xcor() > -350:  # cannot pass through left wall
            self.paddle.bk(35)

    def right(self):
        """ Activate paddle's right movement """
        if self.paddle.xcor() < 350:  # cannot pass through right wall
            self.paddle.fd(35)
