import turtle
import tkinter as tk
from PIL import Image, ImageTk
import time
from ScoreBoard import ScoreBoard
from Paddle import Paddle
from Bricks import Bricks
from Ball import Ball

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
            widget.pack_forget()
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
        self.canvas = tk.Canvas(self.master, width=800, height=800)
        self.canvas.pack(fill="both", expand=True)
        if self.selection == 1:
            self.canvas.create_image(0, 0, image=self.level_backgrounds[0], anchor="nw")
            self.screen = turtle.TurtleScreen(self.canvas)
            self.screen.bgpic('assets/level1_background.png')
            self.screen.update()
        if self.selection == 2:
            self.canvas.create_image(0, 0, image=self.level_backgrounds[1], anchor="nw")
            self.screen = turtle.TurtleScreen(self.canvas)
            self.screen.bgpic('assets/level2_background.png')
        elif self.selection == 3:
            self.canvas.create_image(0, 0, image=self.level_backgrounds[2], anchor="nw")
            self.screen = turtle.TurtleScreen(self.canvas)
            self.screen.bgpic('assets/level3_background.png')
            self.screen.update()
        self.scoreboard = ScoreBoard(screen=self.screen)
        self.game_paddle = Paddle(selection=self.selection, screen=self.screen)
        self.game_ball = Ball(selection=self.selection, screen=self.screen)
        self.brick_color_initialization()
        self.game_bricks = Bricks(selection=self.selection, screen=self.screen)
        self.screen.listen()
        self.start_frame = tk.Frame(self.canvas, background="blue", width=200, height=200)
        self.start_frame.place(x=300, y=400)
        self.start_text = tk.Label(self.canvas, text="Press space to start", fg="white", bg="blue")
        self.start_text.place(x=300, y=450)
        self.screen.onkey(self.game_start, "space")

    def brick_color_initialization(self):
        for index in range(1, 9):
            self.screen.register_shape(fr"assets/brick_{index}.gif")

    def game_win(self):
        self.win_frame = tk.Frame(self.canvas, background="blue", width=200, height=200)
        self.win_frame.place(x=300, y=400)
        self.win_label = tk.Label(self.canvas, text="You Won!", fg="white", bg="blue")
        self.win_label.place(x=350, y=450)
        self.menu_button = tk.Button(self.canvas, text="Main Menu", command=self.select_level)
        self.menu_button.place(x=325, y=500)
        self.quit_button = tk.Button(self.canvas, text="Quit", command=self.master.destroy)
        self.quit_button.place(x=425, y=500)

    def game_over(self):
        self.gameover_frame = tk.Frame(self.canvas, background="blue", width=200, height=200)
        self.gameover_frame.place(x=300, y=400)
        self.gameover_label = tk.Label(self.canvas, text="Game Over", fg="white", bg="blue")
        self.gameover_label.place(x=350, y=450)
        self.menu_button = tk.Button(self.canvas, text="Main Menu", command=self.select_level)
        self.menu_button.place(x=325, y=500)
        self.quit_button = tk.Button(self.canvas, text="Quit", command=self.master.destroy)
        self.quit_button.place(x=425, y=500)

    def game_start(self):
        self.start_text.place_forget()
        self.start_frame.place_forget()
        game_playing = True
        while game_playing:
            time.sleep(1 / 60)
            self.screen.onkey(self.game_paddle.left, "Left")
            self.screen.onkey(self.game_paddle.right, "Right")
            self.game_ball.move()
            self.game_ball.collision_with_walls()
            self.game_ball.collision_with_paddle(self.game_paddle, scoreboard=self.scoreboard)
            self.game_ball.collision_with_bricks(bricks=self.game_bricks, scoreboard=self.scoreboard)
            if self.scoreboard.lives == 0:
                game_playing = False
                self.game_over()
            if not self.game_bricks.bricks:
                game_playing = False
                self.game_win()

if __name__ == "__main__":
    root = tk.Tk()
    root.config(width=800, height=800)
    mainapplication = MainApplication(root)
    root.mainloop()