import tkinter as tk
from tkinter import messagebox, font
import math
import random

class TopSpinGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("TopSpin Game")
        
        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=20)

        self.font = ('Arial', 12)

        self.tokens = list(range(1, 21))
        self.spinner_start = 0
        self.spinner_size = 4
        
        # Set the initial theme
        self.is_dark_mode = True  # Default to dark mode
        self.set_theme()
        
        # Add the theme toggle button
        self.create_button(self.button_frame, "Toggle Dark/Light Mode", self.toggle_theme, self.button_bg)
        
        # Create the action buttons
        self.create_button(self.button_frame, "Rotate Left", self.rotate_left, self.button_bg)
        self.create_button(self.button_frame, "Rotate Right", self.rotate_right, self.button_bg)
        self.create_button(self.button_frame, "Reverse Spinner", self.reverse_spinner, self.button_bg)
        self.create_button(self.button_frame, "Move Spinner Left", self.move_spinner_left, self.button_bg)
        self.create_button(self.button_frame, "Move Spinner Right", self.move_spinner_right, self.button_bg)
        
        # Initialize and generate a solvable random configuration
        self.generate_solvable_configuration()

        # Initial draw of the tokens
        self.draw_tokens()

    def set_theme(self):
        if self.is_dark_mode:
            self.master.configure(bg="#121212")  # Dark background
            self.canvas.configure(bg="#1e1e1e", highlightbackground="#333333")  # Dark canvas
            self.button_bg = "#333333"
            self.button_fg = "#FFFFFF"
            self.highlight_color = "#BB86FC"  # Purple
            self.default_token_color = "#424242"  # Dark gray
            self.text_color = "#FFFFFF"
        else:
            self.master.configure(bg="#f0f0f0")  # Light background
            self.canvas.configure(bg="#FFFFFF", highlightbackground="#cccccc")  # Light canvas
            self.button_bg = "#e0e0e0"
            self.button_fg = "#000000"
            self.highlight_color = "#FFC107"  # Yellow
            self.default_token_color = "#90CAF9"  # Light blue
            self.text_color = "#000000"

        # Update button styles dynamically
        for button in self.button_frame.winfo_children():
            button.configure(bg=self.button_bg, fg=self.button_fg)

        self.draw_tokens()

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.set_theme()

    def draw_tokens(self):
        self.canvas.delete("all")
        center_x, center_y = 250, 250
        radius = 200
        angle_step = 360 / len(self.tokens)

        for i, token in enumerate(self.tokens):
            angle = i * angle_step
            x = center_x + radius * math.cos(angle * math.pi / 180)
            y = center_y + radius * math.sin(angle * math.pi / 180)

            # Determine colors
            if (self.spinner_start <= i < self.spinner_start + self.spinner_size) or \
            (self.spinner_start + self.spinner_size > len(self.tokens) and i < (self.spinner_start + self.spinner_size) % len(self.tokens)):
                fill_color = self.highlight_color  # Highlighted spinner color
                outline_color = "white" if self.is_dark_mode else "black"
            else:
                fill_color = self.default_token_color  # Default token color
                outline_color = self.canvas["bg"]  # Match canvas background

            # Draw tokens with borders
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=fill_color, outline=outline_color, width=3)
            self.canvas.create_text(x, y, text=str(token), font=self.font, fill=self.text_color)

    def create_button(self, parent, text, command, color):
        button = tk.Button(
            parent, 
            text=text, 
            command=command, 
            bg=color, 
            fg="white", 
            font=self.font, 
            activebackground="#e0e0e0", 
            activeforeground="black", 
            pady=5, 
            padx=10, 
            bd=0
        )
        button.pack(side=tk.LEFT, padx=5)

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

    def generate_solvable_configuration(self):
        # Start with the goal configuration
        current_configuration = self.tokens[:]
        
        # Perform an even number of swaps to generate a solvable configuration
        for _ in range(random.randint(1, 5)):  # Perform 1 to 5 even swaps
            i, j = random.sample(range(len(self.tokens)), 2)
            # Swap i and j
            current_configuration[i], current_configuration[j] = current_configuration[j], current_configuration[i]
            # Perform another swap to maintain even parity
            i, j = random.sample(range(len(self.tokens)), 2)
            current_configuration[i], current_configuration[j] = current_configuration[j], current_configuration[i]
        
        self.tokens = current_configuration

if __name__ == "__main__":
    root = tk.Tk()
    app = TopSpinGUI(root)
    root.mainloop()
