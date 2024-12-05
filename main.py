import tkinter as tk
from tkinter import messagebox
import math

class TopSpinGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("TopSpin Game")

        # Initialize game state
        self.tokens = list(range(1, 21))  # Example with 8 tokens
        self.spinner_size = 4

        # Create UI elements
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()

        self.draw_tokens()

        self.rotate_left_button = tk.Button(self.master, text="Rotate Left", command=self.rotate_left)
        self.rotate_left_button.pack(side=tk.LEFT)

        self.rotate_right_button = tk.Button(self.master, text="Rotate Right", command=self.rotate_right)
        self.rotate_right_button.pack(side=tk.LEFT)

        self.reverse_button = tk.Button(self.master, text="Reverse Spinner", command=self.reverse_spinner)
        self.reverse_button.pack(side=tk.LEFT)

    def draw_tokens(self):
        self.canvas.delete("all")
        center_x, center_y = 200, 200
        radius = 150
        angle_step = 360 / len(self.tokens)

        for i, token in enumerate(self.tokens):
            angle = i * angle_step
            x = center_x + radius * math.cos(angle * math.pi / 180)
            y = center_y + radius * math.sin(angle * math.pi / 180)
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
            self.canvas.create_text(x, y, text=str(token))

    def rotate_left(self):
        self.tokens = self.tokens[1:] + [self.tokens[0]]
        self.draw_tokens()

    def rotate_right(self):
        self.tokens = [self.tokens[-1]] + self.tokens[:-1]
        self.draw_tokens()

    def reverse_spinner(self):
        self.tokens[:self.spinner_size] = reversed(self.tokens[:self.spinner_size])
        self.draw_tokens()

if __name__ == "__main__":
    root = tk.Tk()
    app = TopSpinGUI(root)
    root.mainloop()
