import turtle
import tkinter as tk
from PIL import Image, ImageTk

class Paddle:
    def __init__(self, selection, screen):
        self.paddle_image = r"assets/paddle_1.gif"
        screen.register_shape(self.paddle_image)
        self.paddle = turtle.RawTurtle(screen, shape=self.paddle_image, visible=False)
        self.paddle.penup()
        self.paddle.goto(0,-380)
        self.paddle.showturtle()

    def left(self):
        self.paddle.bk(25)
    def right(self):
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
            self.game_paddle = Paddle(selection=self.selection, screen=self.screen)
            self.game_start()
        if self.selection == 2:
            pass
        elif self.selection == 3:
            pass

    def game_start(self):
        self.screen.listen()
        self.screen.onkey(self.game_paddle.left, "Left")
        self.screen.onkey(self.game_paddle.right, "Right")

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Breakout Game")
        self.start_button = tk.Button(self.master, text="Start Game", command=self.select_level)
        self.start_button.grid(row=0, column=1)
        self.level1_background = tk.PhotoImage(file="assets/level1_background.png")
        self.level_backgrounds = [self.level1_background]

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