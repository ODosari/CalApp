"""
Application Name: CalApp
Version: 0.1
Created by: Obaid Aldosari
GitHub: https://github.com/ODosari
"""

import math
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox


class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator Application")
        self.root.geometry("975x500+500+200")
        self.root.resizable(width=True, height=True)

        custom_font = tkFont.Font(family="IBM Plex Mono", size=30, weight="bold")

        # Create the entry box
        self.label = tk.Label(self.root, width=44, justify="center", bg='black', fg='white', font=custom_font)
        self.label.grid(row=0, column=0, columnspan=6)
        self.label.focus_set()

        # Create the buttons
        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("√", 1, 4),
            ("(", 1, 5),  # Left parenthesis
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("ln", 2, 4),
            (")", 2, 5),  # Right parenthesis
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("sin", 3, 4),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
            ("C", 4, 4),
        ]
        for button in buttons:
            text, row, col = button
            tk.Button(
                self.root,
                text=text,
                width=7,
                height=2,
                font=custom_font,
                bg='white',
                fg='green',
                command=lambda t=text: self.on_button_click(t),
            ).grid(row=row, column=col)

        self.history = []

        tk.Button(
            self.root,
            text="Clear History",
            width=15,
            height=2,
            font=custom_font,
            bg='black',
            fg='green',
            command=self.clear_history,
        ).grid(row=6, column=0, columnspan=2)

        tk.Button(
            self.root,
            text="Show History",
            width=15,
            height=2,
            font=custom_font,
            bg='black',
            fg='green',
            command=self.show_history,
        ).grid(row=6, column=3, columnspan=2)

        self.root.mainloop()

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.label['text'])
                self.history.append(self.label['text'] + " = " + str(result))
                self.label.config(text=str(result))
            except Exception as e:
                self.label.config(text="Error: " + str(e))
        elif text == "C":
            self.label.config(text="")
            self.history = []
        elif text == "√":
            try:
                value = float(self.label['text'])
                result = math.sqrt(value)
                self.label.config(text=str(result))
            except ValueError:
                self.label.config(text="Error: Invalid Input")
        elif text == "ln":
            try:
                value = float(self.label['text'])
                result = math.log(value)
                self.label.config(text=str(result))
            except ValueError:
                self.label.config(text="Error: Invalid Input")
        elif text == "sin":
            try:
                value = float(self.label['text'])
                result = math.sin(value)
                self.label.config(text=str(result))
            except ValueError:
                self.label.config(text="Error: Invalid Input")
        else:
            self.label.config(text=self.label['text'] + text)

    def clear_history(self):
        self.history = []
        self.label.config(text="")

    def show_history(self):
        history_text = "\n".join(self.history)
        messagebox.showinfo("Calculation History", history_text)
        self.root.focus_force()


if __name__ == "__main__":
    app = CalculatorApp()
