import turtle
import tkinter as tk
from PIL import Image, ImageTk
import random
import time

class Brick():
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
    def __init__(self, selection, screen, color):
        self.bricks = []
        self.brick_generation(selection=selection, screen=screen, color=color)


    def brick_generation(self, selection, screen, color):
        if selection == 1:
            rows = 8
            cols = 7
            for row in range(rows):
                for col in range(cols):
                    x = -300 + col * 100
                    y = 300 - row * 30
                    brick = Brick(screen, color)
                    self.bricks.append(brick)
                    brick.brick.goto(x,y)
        elif selection == 2:
            row1 = ["x", "x", "x", "x", "x", "x", "x", ]
            row2 = ["x", "", "", "", "", "", "x",]
            for row in range(1,10):
                if row % 2 != 0:
                    col = 0
                    for mark in row1:
                        if mark == "x":
                            x = -300 + col * 100
                            y = 300 - row * 30
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
                            brick = Brick(screen, color)
                            self.bricks.append(brick)
                            brick.brick.goto(x, y)
                            col += 1
                        else:
                            col += 1




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

    def collision_with_paddle(self, paddle):
        if self.ball.ycor() < -375:
            self.ball.hideturtle()
            self.ball.goto(0,-50)
            self.ball.showturtle()
        elif self.ball.ycor() < -355:
            if self.ball.xcor() <= paddle.paddle.xcor() + 50 and self.ball.xcor() >= paddle.paddle.xcor() - 50:
                self.ball_y_move *= -1

    def collision_with_bricks(self, bricks):
        for brick in bricks.bricks:
            if self.ball.distance(brick.brick) < 50:
                if (self.ball.xcor() < brick.brick.xcor() + 50 and self.ball.xcor() > brick.brick.xcor() - 50):
                    if self.ball.ycor() < brick.brick.ycor() - 16:
                        self.ball_y_move *= -1
                    elif (self.ball.ycor() < brick.brick.ycor()-16 and self.ball.ycor() > brick.brick.ycor()+16):
                        self.ball_x_move *= -1
                    elif self.ball.ycor() > brick.brick.ycor() + 16:
                        self.ball_y_move *= -1
                    brick.brick.clear()
                    brick.brick.hideturtle()
                    bricks.bricks.remove(brick)
                    time.sleep(0.01)


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
            self.paddle.bk(25)
    def right(self):
        if self.paddle.xcor() < 350:
            self.paddle.fd(25)


class Game:
    def __init__(self, master, selection, level_backgrounds):
        self.selection = selection
        self.master = master
        self.canvas = tk.Canvas(self.master, width=800, height=800)
        self.canvas.pack(fill="both", expand=True)
        if self.selection == 1:
            self.canvas.create_image(0, 0, image=level_backgrounds[0], anchor="nw")
            self.screen = turtle.TurtleScreen(self.canvas)
            self.screen.bgpic('assets/level1_background.png')
            self.screen.update()
        if self.selection == 2:
            self.canvas.create_image(0, 0, image=level_backgrounds[1], anchor="nw")
            self.screen = turtle.TurtleScreen(self.canvas)
            self.screen.bgpic('assets/level2_background.png')
        elif self.selection == 3:
            self.canvas.create_image(0, 0, image=level_backgrounds[2], anchor="nw")
            self.screen = turtle.TurtleScreen(self.canvas)
            self.screen.bgpic('assets/level3_background.png')
            self.screen.update()
        self.game_paddle = Paddle(selection=self.selection, screen=self.screen)
        self.game_ball = Ball(selection=self.selection, screen=self.screen)
        self.brick_color = r"assets/brick_1.gif"
        self.screen.register_shape(self.brick_color)
        self.game_bricks = Bricks(selection=self.selection, screen=self.screen, color=self.brick_color)
        self.screen.listen()
        self.screen.onkey(self.game_start, "space")
        global game_playing
        game_playing = True

    def game_start(self):
        while game_playing:
            time.sleep(1 / 60)
            self.screen.onkey(self.game_paddle.left, "Left")
            self.screen.onkey(self.game_paddle.right, "Right")
            self.game_ball.move()
            self.game_ball.collision_with_walls()
            self.game_ball.collision_with_paddle(self.game_paddle)
            self.game_ball.collision_with_bricks(bricks=self.game_bricks)

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Breakout Game")
        self.start_button = tk.Button(self.master, text="Start Game", command=self.select_level)
        self.start_button.grid(row=0, column=1)
        self.level1_background = tk.PhotoImage(file="assets/level1_background.png")
        self.level2_background = tk.PhotoImage(file="assets/level2_background.png")
        self.level3_background = tk.PhotoImage(file="assets/level3_background.png")
        self.level_backgrounds = [self.level1_background, self.level2_background, self.level3_background]

    def select_level(self):
        for widget in root.winfo_children():
            widget.grid_forget()
        self.var = tk.IntVar()
        self.select_title = tk.Label(self.master, text="Select Level")
        self.select_title.grid(row=0, column=1)
        self.selection_label = tk.Label(self.master, text="")
        self.selection_label.grid(row=2, column=1)

        self.level1_image = ImageTk.PhotoImage(Image.open("assets/level1_preview.png"))
        self.level1_button = tk.Radiobutton(self.master, variable=self.var, value=1, indicatoron=0,
                                            image=self.level1_image, command=self.update_selection)
        self.level1_button.grid(row=1, column=0)
        self.level2_image = ImageTk.PhotoImage(Image.open("assets/level2_preview.png"))
        self.level2_button = tk.Radiobutton(self.master, variable=self.var, value=2, indicatoron=0,
                                            image=self.level2_image, command=self.update_selection)
        self.level2_button.grid(row=1, column=1)
        self.level3_image = ImageTk.PhotoImage(Image.open("assets/level3_preview.png"))
        self.level3_button = tk.Radiobutton(self.master, variable=self.var, value=3, indicatoron=0,
                                            image=self.level3_image, command=self.update_selection)
        self.level3_button.grid(row=1, column=2)
        self.start_game_button = tk.Button(self.master, text="Start Game", command=self.start_game)
        self.start_game_button.grid(row=3, column=1)
    def update_selection(self):
        self.selection = self.var.get()
        if self.selection == 1:
            self.selection_label.config(text="You have selected Level 1")
        elif self.selection == 2:
            self.selection_label.config(text="You have selected Level 2")
        elif self.selection == 3:
            self.selection_label.config(text="You have selected Level 3")

    def start_game(self):
        for widget in root.winfo_children():
            widget.grid_forget()
        game = Game(master=root, selection=self.var.get(), level_backgrounds=self.level_backgrounds)


if __name__ == "__main__":
    root = tk.Tk()
    root.config(width=800, height=800)
    mainapplication = MainApplication(root)
    root.mainloop()