import tkinter as tk
from tkinter import messagebox
import math  # Import the math module for trigonometric functions

class TopSpinGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("TopSpin Game")

        # Initialize game state with 20 tokens
        self.tokens = list(range(1, 21))  # Start with 20 numbers
        self.spinner_size = 4  # Spinner covers 4 numbers
        self.spinner_start = 0  # Initial spinner position

        # Create UI elements
        self.canvas = tk.Canvas(self.master, width=500, height=500)  # Increase canvas size for 20 tokens
        self.canvas.pack()

        self.draw_tokens()

        self.rotate_left_button = tk.Button(self.master, text="Rotate Left", command=self.rotate_left)
        self.rotate_left_button.pack(side=tk.LEFT)

        self.rotate_right_button = tk.Button(self.master, text="Rotate Right", command=self.rotate_right)
        self.rotate_right_button.pack(side=tk.LEFT)

        self.reverse_button = tk.Button(self.master, text="Reverse Spinner", command=self.reverse_spinner)
        self.reverse_button.pack(side=tk.LEFT)

        self.spinner_left_button = tk.Button(self.master, text="Move Spinner Left", command=self.move_spinner_left)
        self.spinner_left_button.pack(side=tk.LEFT)

        self.spinner_right_button = tk.Button(self.master, text="Move Spinner Right", command=self.move_spinner_right)
        self.spinner_right_button.pack(side=tk.LEFT)

    def draw_tokens(self):
        self.canvas.delete("all")
        center_x, center_y = 250, 250  # Adjust center to fit larger canvas
        radius = 200  # Increase radius to fit more tokens
        angle_step = 360 / len(self.tokens)  # Adjust angle step dynamically

        for i, token in enumerate(self.tokens):
            angle = i * angle_step
            x = center_x + radius * math.cos(angle * math.pi / 180)
            y = center_y + radius * math.sin(angle * math.pi / 180)

            # Highlight tokens in spinner range
            if (self.spinner_start <= i < self.spinner_start + self.spinner_size) or \
            (self.spinner_start + self.spinner_size > len(self.tokens) and i < (self.spinner_start + self.spinner_size) % len(self.tokens)):
                fill_color = "lightgreen"  # Highlighted color for spinner range
            else:
                fill_color = "lightblue"   # Default color

            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=fill_color)
            self.canvas.create_text(x, y, text=str(token))

    def rotate_left(self):
        self.tokens = self.tokens[1:] + [self.tokens[0]]
        self.spinner_start = (self.spinner_start - 1) % len(self.tokens)  # Adjust spinner position
        self.draw_tokens()

    def rotate_right(self):
        self.tokens = [self.tokens[-1]] + self.tokens[:-1]
        self.spinner_start = (self.spinner_start + 1) % len(self.tokens)  # Adjust spinner position
        self.draw_tokens()

    def reverse_spinner(self):
         # Calculate the end index, considering wrap-around
        end = self.spinner_start + self.spinner_size
        if end <= len(self.tokens):
            # If no wrap-around, reverse normally
            self.tokens[self.spinner_start:end] = reversed(self.tokens[self.spinner_start:end])
        else:
            # Handle wrap-around by reversing in two parts
            part1 = self.tokens[self.spinner_start:]  # Tokens from spinner_start to the end
            part2 = self.tokens[:end % len(self.tokens)]  # Tokens from the beginning to wrap-around index
            reversed_section = list(reversed(part1 + part2))  # Combine and reverse both parts
            self.tokens[self.spinner_start:] = reversed_section[:len(part1)]  # Update part1
            self.tokens[:end % len(self.tokens)] = reversed_section[len(part1):]  # Update part2
        self.draw_tokens()

    def move_spinner_left(self):
        # Move spinner position left (counter-clockwise)
        self.spinner_start = (self.spinner_start - 1) % len(self.tokens)
        self.draw_tokens()

    def move_spinner_right(self):
        # Move spinner position right (clockwise)
        self.spinner_start = (self.spinner_start + 1) % len(self.tokens)
        self.draw_tokens()

if __name__ == "__main__":
    root = tk.Tk()
    app = TopSpinGUI(root)
    root.mainloop()
