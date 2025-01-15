from tkinter import *
import random
from tkinter import simpledialog
import pygame  # Import pygame for sound playback

class SnakeAndLadder:
    def __init__(self, root):
        pygame.mixer.init()  # Initialize the pygame mixer for sound
        self.root = root
        self.root.title("Snake and Ladder Game")
        self.root.geometry("900x650")

        # Game board
        self.board = Canvas(self.root, width=600, height=600, bg="lightblue")
        self.board.grid(row=0, column=0, rowspan=10, columnspan=10, padx=10, pady=10)

        # Player data
        self.players = []
        self.current_player = 0
        self.player_colors = ["red", "blue", "green", "yellow"]

        # Snakes and Ladders
        self.snakes = {17: 7, 54: 19, 62: 18, 95: 56, 98: 64}
        self.ladders = {3: 20, 11: 28, 60: 85, 71: 91}

        # Create game board
        self.draw_board()

        # Dice image placeholder
        self.dice_image = Label(self.root, text="🎲", font=("Helvetica", 20))
        self.dice_image.grid(row=0, column=11, padx=10)

        # Buttons
        self.roll_button = Button(self.root, text="Roll Dice", command=self.roll_dice, width=10)
        self.roll_button.grid(row=1, column=11, pady=5)
        self.restart_button = Button(self.root, text="Restart", command=self.restart_game, width=10)
        self.restart_button.grid(row=2, column=11, pady=5)
        self.quit_button = Button(self.root, text="Quit", command=self.root.quit, width=10)
        self.quit_button.grid(row=3, column=11, pady=5)

        # Player information
        self.player_info_label = Label(self.root, text="", font=("Helvetica", 12), fg="blue")
        self.player_info_label.grid(row=4, column=11, pady=10)

        # Add players
        self.add_players()

    def draw_board(self):
        for i in range(10):
            for j in range(10):
                number = 100 - (i * 10 + j) if i % 2 == 0 else 91 - (i * 10) + j
                x1, y1 = j * 60, i * 60
                x2, y2 = x1 + 60, y1 + 60
                self.board.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                self.board.create_text(x1 + 30, y1 + 30, text=str(number), font=("Helvetica", 10))

        for start, end in self.snakes.items():
            self.draw_snake_or_ladder(start, end, "red")

        for start, end in self.ladders.items():
            self.draw_snake_or_ladder(start, end, "green")

    def draw_snake_or_ladder(self, start, end, color):
        x1, y1 = self.get_coordinates(start)
        x2, y2 = self.get_coordinates(end)
        self.board.create_line(x1, y1, x2, y2, fill=color, width=3, arrow=LAST)

    def get_coordinates(self, position):
        row = 10 - (position - 1) // 10
        col = (position - 1) % 10
        if row % 2 == 0:
            col = 9 - col  # Reverse column for even rows
        x = col * 60 + 30
        y = (row - 1) * 60 + 30
        return x, y

    def add_players(self):
        num_players = simpledialog.askinteger(
            "Player Setup",
            "Enter number of players (2-4):",
            parent=self.root,
            minvalue=2,
            maxvalue=4
        )
        if num_players is None:
            self.root.quit()
            return

        for i in range(num_players):
            name = simpledialog.askstring(
                "Player Setup",
                f"Enter player {i+1} name:",
                parent=self.root
            )
            if not name:
                name = f"Player {i+1}"
            self.players.append({"name": name, "position": 1, "token": None})

    def roll_dice(self):
        dice_roll = random.randint(1, 6)
        self.update_dice_image(dice_roll)
        self.play_sound("dice_roll.wav")  # Play dice roll sound

        current_player = self.players[self.current_player]
        new_position = current_player["position"] + dice_roll

        if new_position > 100:
            self.player_info_label.config(text=f"{current_player['name']}, you cannot exceed 100!")
            return

        if new_position in self.snakes:
            new_position = self.snakes[new_position]
            self.play_sound("snake.wav")  # Play snake sound
            self.player_info_label.config(text=f"{current_player['name']} slithered down to {new_position}!")
        elif new_position in self.ladders:
            new_position = self.ladders[new_position]
            self.play_sound("ladder.wav")  # Play ladder sound
            self.player_info_label.config(text=f"{current_player['name']} climbed up to {new_position}!")

        current_player["position"] = new_position

        if new_position == 100:
            self.play_sound("win.wav")  # Play win sound
            self.player_info_label.config(text=f"{current_player['name']} wins!")
            self.roll_button.config(state=DISABLED)
            return

        self.update_player_position()

        self.current_player = (self.current_player + 1) % len(self.players)
        self.player_info_label.config(text=f"{self.players[self.current_player]['name']}'s turn.")

    def update_dice_image(self, dice_roll):
        self.dice_image.config(text=f"🎲 {dice_roll}")

    def update_player_position(self):
        for player in self.players:
            if player["token"]:
                self.board.delete(player["token"])

        for player in self.players:
            x, y = self.get_coordinates(player["position"])
            player["token"] = self.board.create_oval(x - 10, y - 10, x + 10, y + 10, fill=self.player_colors[self.players.index(player)])

    def play_sound(self, sound_file):
        pygame.mixer.Sound(sound_file).play()

    def restart_game(self):
        for player in self.players:
            player["position"] = 1
        self.current_player = 0
        self.roll_button.config(state=NORMAL)
        self.player_info_label.config(text="")
        self.update_player_position()

if __name__ == "__main__":
    root = Tk()
    game = SnakeAndLadder(root)
    root.mainloop()
