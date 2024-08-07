import turtle
import random


class Brick:
    def __init__(self, screen, color):
        """ Each brick turtle is created and its appearance is changed """
        self.brick = turtle.RawTurtle(screen)
        self.brick.shape(color)
        self.brick.penup()


class Bricks:
    def __init__(self, selection, screen):
        """ Create list of all bricks and generate them """
        self.bricks = []
        self.brick_generation(selection=selection, screen=screen)

    @staticmethod
    def color_pick():
        """ Returns a randomized brick color image """
        color_index = random.randint(1, 8)  # There are brick images indexed 1 to 8
        brick_image = fr"assets/brick_{color_index}.gif"
        return brick_image

    def brick_generation(self, selection, screen):
        """ Generates the bricks in different layouts depending on the level selected """
        if selection == 1:  # Level 1
            # Layout
            rows = 8
            cols = 7
            # Generate the bricks for every row
            for row in range(rows):
                for col in range(cols):
                    x = -300 + col * 100
                    y = 300 - row * 30
                    # Pick the brick's color
                    color = self.color_pick()
                    brick = Brick(screen, color)
                    # Added to the list of bricks and their position is set
                    self.bricks.append(brick)
                    brick.brick.goto(x, y)
        elif selection == 2:  # Level 2
            # Layout
            row1 = ["x", "x", "x", "x", "x", "x", "x"]
            row2 = ["x", "", "", "", "", "", "x",]
            # Generate 10 rows with the rows above
            for row in range(1, 10):
                # For every odd row, layout of row1 is used
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
                            # Keep count of amounts of bricks generated to create the space between bricks needed
                            col += 1
                        else:
                            # Keep count of amounts of spaces to create the space between bricks needed
                            col += 1
                else:
                    # For every even row, layout of row2 is used
                    col = 0
                    for mark in row2:
                        if mark == "x":
                            x = -300 + col * 100
                            y = 300 - row * 30
                            # Pick the brick's color
                            color = self.color_pick()
                            brick = Brick(screen, color)
                            # Added to the list of bricks and their position is set
                            self.bricks.append(brick)
                            brick.brick.goto(x, y)
                            # Keep count of amounts of bricks generated to create the space between bricks needed
                            col += 1
                        else:
                            # Keep count of amounts of spaces to create the space between bricks needed
                            col += 1
        elif selection == 3:  # Level 3
            # Layout for every row
            row1 = ["x", "x", "", "x", "x", "", "x"]
            # Generate the bricks of seven rows
            for row in range(1, 7):
                col = 0
                for mark in row1:
                    if mark == "x":
                        x = -300 + col * 100
                        y = 300 - row * 30
                        # Pick the brick's color
                        color = self.color_pick()
                        brick = Brick(screen, color)
                        # Added to the list of bricks and their position is set
                        self.bricks.append(brick)
                        brick.brick.goto(x, y)
                        # Keep count of amounts of bricks generated to create the space between bricks needed
                        col += 1
                    else:
                        # Keep count of amounts of spaces to create the space between bricks needed
                        col += 1

            # Generate 5 more rows with a space between the 7 and 5 rows
            for row in range(1, 5):
                col = 0
                for mark in row1:
                    if mark == "x":
                        x = -300 + col * 100
                        y = 69 - row * 30
                        # Pick the brick's color
                        color = self.color_pick()
                        brick = Brick(screen, color)
                        # Added to the list of bricks and their position is set
                        self.bricks.append(brick)
                        brick.brick.goto(x, y)
                        # Keep count of amounts of bricks generated to create the space between bricks needed
                        col += 1
                    else:
                        # Keep count of amounts of spaces to create the space between bricks needed
                        col += 1
