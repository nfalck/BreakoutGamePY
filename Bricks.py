import turtle
import random
class Brick:
    def __init__(self, screen, color):
        self.brick = turtle.RawTurtle(screen)
        self.brick.shape(color)
        self.brick.penup()
        self.brick_top = self.brick.ycor()+33
        self.brick_right = self.brick.xcor()+30
        self.brick_left = self.brick.xcor()-30
        self.brick_bottom = self.brick.ycor()-33


    def generate(self, x, y):
        self.brick.goto(x,y)

class Bricks:
    def __init__(self, selection, screen):
        self.bricks = []
        self.brick_generation(selection=selection, screen=screen)

    def color_pick(self):
        color_index = random.randint(1,8)
        brick_image = fr"assets/brick_{color_index}.gif"
        return brick_image

    def brick_generation(self, selection, screen):
        if selection == 1:
            rows = 8
            cols = 7
            for row in range(rows):
                for col in range(cols):
                    x = -300 + col * 100
                    y = 300 - row * 30
                    color = self.color_pick()
                    brick = Brick(screen, color)
                    self.bricks.append(brick)
                    brick.brick.goto(x,y)
        elif selection == 2:
            row1 = ["x", "x", "x", "x", "x", "x", "x"]
            row2 = ["x", "", "", "", "", "", "x",]
            for row in range(1,10):
                if row % 2 != 0:
                    col = 0
                    for mark in row1:
                        if mark == "x":
                            x = -300 + col * 100
                            y = 300 - row * 30
                            color = self.color_pick()
                            brick = Brick(screen, color)
                            self.bricks.append(brick)
                            brick.brick.goto(x, y)
                            col += 1
                        else:
                            col += 1
                else:
                    col = 0
                    for mark in row2:
                        if mark == "x":
                            x = -300 + col * 100
                            y = 300 - row * 30
                            color = self.color_pick()
                            brick = Brick(screen, color)
                            self.bricks.append(brick)
                            brick.brick.goto(x, y)
                            col += 1
                        else:
                            col += 1
        elif selection == 3:
            row1 = ["x", "x", "", "x", "x", "", "x"]
            space = ["", "", "", "", "", "", ""]
            for row in range(1,7):
                col = 0
                for mark in row1:
                    if mark == "x":
                        x = -300 + col * 100
                        y = 300 - row * 30
                        color = self.color_pick()
                        brick = Brick(screen, color)
                        self.bricks.append(brick)
                        brick.brick.goto(x, y)
                        col += 1
                    else:
                        col += 1

            for row in range(1,5):
                col = 0
                for mark in row1:
                    if mark == "x":
                        x = -300 + col * 100
                        y = 69 - row * 30
                        color = self.color_pick()
                        brick = Brick(screen, color)
                        self.bricks.append(brick)
                        brick.brick.goto(x, y)
                        col += 1
                    else:
                        col += 1