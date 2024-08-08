import turtle
import tkinter as tk
import customtkinter as ctk  # To make the buttons visible for Mac as well
from PIL import Image, ImageTk
import time
from ScoreBoard import ScoreBoard
from Paddle import Paddle
from Bricks import Bricks
from Ball import Ball


class MainApplication:
    def __init__(self, master):
        # Main Menu layout
        self.master = master
        self.master.title("Breakout Game")
        self.startmenu_text = tk.Label(self.master, text="Breakout Game", font=('Lexend', 18, 'normal'), fg="white",
                                       background="#AF47D2", pady=50, padx=50)
        self.startmenu_text.grid(row=0, column=0)
        self.start_button = ctk.CTkButton(self.master, text="Start Game", command=self.select_level, fg_color="#26355D",
                                          corner_radius=10, border_width=2, bg_color="#AF47D2", border_color="white")
        self.start_button.grid(row=1, column=0)

        # Background images for every level
        self.level1_background = tk.PhotoImage(file="assets/level1_background.png")
        self.level2_background = tk.PhotoImage(file="assets/level2_background.png")
        self.level3_background = tk.PhotoImage(file="assets/level3_background.png")

        #  Level Selection Widgets for select_level
        self.select_title = tk.Label(self.master, text="Select Level", fg="white", background="#AF47D2")  # Title
        self.level1_image = ImageTk.PhotoImage(Image.open("assets/level1_preview.png"))  # Preview of level 1
        self.level2_image = ImageTk.PhotoImage(Image.open("assets/level2_preview.png"))  # Preview of level 2
        self.level3_image = ImageTk.PhotoImage(Image.open("assets/level3_preview.png"))  # Preview of level 3
        self.var = tk.IntVar()  # Value of level selected
        self.level1_button = self.level1_button = tk.Radiobutton(self.master, variable=self.var, value=1,
                                                                 indicatoron=False, image=self.level1_image,
                                                                 command=self.update_selection)
        self.level2_button = self.level2_button = tk.Radiobutton(self.master, variable=self.var, value=2,
                                                                 indicatoron=False, image=self.level2_image,
                                                                 command=self.update_selection)
        self.level3_button = self.level3_button = tk.Radiobutton(self.master, variable=self.var, value=3,
                                                                 indicatoron=False, image=self.level3_image,
                                                                 command=self.update_selection)
        self.selection_label = tk.Label(self.master, text="",
                                        background="#AF47D2", fg="white")  # Indicates which level is selected
        self.start_game_button = ctk.CTkButton(self.master, text="Start Game", command=self.initialize_game,
                                               fg_color="#26355D", corner_radius=10, border_width=2,
                                               bg_color="#AF47D2", border_color="white")

        self.selection = None  # initialized in update_selection

        # Game Widgets for start_game
        self.canvas = tk.Canvas(self.master, width=800, height=800)
        self.start_frame = tk.Frame(self.canvas, background="#AF47D2", width=200, height=200)
        self.start_text = tk.Label(self.canvas, text="Press space to start", fg="white", bg="#AF47D2")

        # Game Assets that will be initialized in start_game
        self.screen = None  # TurtleScreen
        self.scoreboard = None
        self.game_paddle = None
        self.game_ball = None
        self.game_bricks = None

        # Game Win Widgets for game_win
        self.win_frame = tk.Frame(self.canvas, background="#AF47D2", width=200, height=200)
        self.win_label = tk.Label(self.canvas, text="You Won!", fg="white", bg="#AF47D2")

        # Gameover Widgets for game_over
        self.gameover_frame = tk.Frame(self.canvas, background="#AF47D2", width=200, height=200)
        self.gameover_label = tk.Label(self.canvas, text="Game Over", fg="white", bg="#AF47D2")

    def select_level(self):
        """ Generate the menu of level selection """
        for widget in root.winfo_children():
            widget.grid_forget()
            widget.pack_forget()
            widget.place_forget()
        self.select_title.grid(row=0, column=1)
        self.selection_label.grid(row=2, column=1)
        self.level1_button.grid(row=1, column=0)
        self.level2_button.grid(row=1, column=1)
        self.level3_button.grid(row=1, column=2)
        self.start_game_button.grid(row=3, column=1)

    def update_selection(self):
        """ Update the selection label to indicate the level chosen """
        self.selection = self.var.get()  # The value of the level chosen
        if self.selection == 1:
            self.selection_label.config(text="You have selected Level 1")
        elif self.selection == 2:
            self.selection_label.config(text="You have selected Level 2")
        elif self.selection == 3:
            self.selection_label.config(text="You have selected Level 3")

    def initialize_game(self):
        """ Create the game window and assets """
        # Clear widgets from level selection menu
        for widget in root.winfo_children():
            widget.grid_forget()
            widget.place_forget()

        for widget in self.canvas.winfo_children():
            widget.grid_forget()
            widget.place_forget()

        # Pack the canvas to place the TurtleScreen on
        self.canvas.pack(fill="both", expand=True)

        # Set the background depending on the level selected and update it to become visible
        if self.selection == 1:
            self.canvas.create_image(0, 0, image=self.level1_background, anchor="nw")
            self.screen = turtle.TurtleScreen(self.canvas)
            self.screen.bgpic('assets/level1_background.png')
            self.screen.update()

        if self.selection == 2:
            self.canvas.create_image(0, 0, image=self.level2_background, anchor="nw")
            self.screen = turtle.TurtleScreen(self.canvas)
            self.screen.bgpic('assets/level2_background.png')

        elif self.selection == 3:
            self.canvas.create_image(0, 0, image=self.level3_background, anchor="nw")
            self.screen = turtle.TurtleScreen(self.canvas)
            self.screen.bgpic('assets/level3_background.png')
            self.screen.update()

        # Generate the scoreboard, paddle, ball and bricks
        self.scoreboard = ScoreBoard(screen=self.screen)
        self.game_paddle = Paddle(selection=self.selection, screen=self.screen)
        self.game_ball = Ball(selection=self.selection, screen=self.screen)

        self.brick_color_initialization()  # Register all the brick images before creating the bricks
        self.game_bricks = Bricks(selection=self.selection, screen=self.screen)

        # Start "popup" to instruct the player to press space in order to start playing
        self.start_frame.place(x=300, y=300)
        self.start_text.place(x=315, y=380)

        # Screen starts listening for any key presses
        self.screen.listen()
        self.screen.onkey(self.game_start, "space")  # Game starts when space is pressed

    def brick_color_initialization(self):
        """ Register all brick images so they can be used """
        for index in range(1, 9):
            self.screen.register_shape(fr"assets/brick_{index}.gif")

    def game_win(self):
        """ Generate the win "popup" to indicate player's win and give option to go to main menu or
        quit the application """
        # Place the widgets needed
        self.win_frame.place(x=300, y=400)
        self.win_label.place(x=355, y=350)
        self.menu_button = ctk.CTkButton(self.canvas, text="Main Menu", command=self.select_level, width=60,
                                         fg_color="#26355D", corner_radius=10, bg_color="#AF47D2")
        self.menu_button.place(x=315, y=400)
        self.quit_button = ctk.CTkButton(self.canvas, text="Quit", command=self.master.destroy, width=30,
                                         fg_color="#26355D", corner_radius=10, bg_color="#AF47D2")
        self.quit_button.place(x=435, y=400)

    def game_over(self):
        """ Generate the gameover "popup" to indicate player's loss and give option to go to main menu or
        quit the application """
        # Place the widgets needed
        self.gameover_frame.place(x=300, y=300)
        self.gameover_label.place(x=355, y=350)
        self.menu_button = ctk.CTkButton(self.canvas, text="Main Menu", command=self.select_level, width=60,
                                         fg_color="#26355D", corner_radius=10, bg_color="#AF47D2")
        self.menu_button.place(x=315, y=400)
        self.quit_button = ctk.CTkButton(self.canvas, text="Quit", command=self.master.destroy, width=30,
                                         fg_color="#26355D", corner_radius=10, bg_color="#AF47D2")
        self.quit_button.place(x=435, y=400)

    def game_start(self):
        """ Start the game and its logic when player presses space """
        # Remove the start "popup"
        self.start_text.place_forget()
        self.start_frame.place_forget()

        # Set the game logic
        game_playing = True
        while game_playing:
            time.sleep(1 / 60)
            # Listen for paddle left movement
            self.screen.onkey(self.game_paddle.left, "Left")
            # Listen for paddle right movement
            self.screen.onkey(self.game_paddle.right, "Right")

            # Activate ball movement and check its collisions
            self.game_ball.move()
            self.game_ball.collision_with_walls()
            self.game_ball.collision_with_paddle(self.game_paddle, scoreboard=self.scoreboard)
            self.game_ball.collision_with_bricks(bricks=self.game_bricks, scoreboard=self.scoreboard)

            # Check if lives == 0, if so gameover
            if self.scoreboard.lives == 0:
                game_playing = False
                self.game_over()

            # Check if there are any bricks left, otherwise game is won
            if not self.game_bricks.bricks:
                game_playing = False
                self.game_win()


if __name__ == "__main__":
    # Create the tkinter window
    root = tk.Tk()
    root.config(width=800, height=800, background="#AF47D2")
    # Create an instance of the MainApplication class and start the main event loop
    mainapplication = MainApplication(root)
    root.mainloop()
