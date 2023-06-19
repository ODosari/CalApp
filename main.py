"""
Application Name: CalApp
Version: 0.1
Created by: Obaid Aldosari
Github: https://github.com/ODosari
"""

import math
import tkinter as tk
import tkinter.font as tkFont


class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator Application")
        self.root.geometry("670x600+500+200")
        self.root.resizable(width=True, height=True)

        custom_font = tkFont.Font(family="IBM Plex Mono", size=30, weight="bold")

        # Create the entry box
        self.label = tk.Label(self.root, width=35, justify="center", bg='gray', fg='black', font=custom_font)
        self.label.grid(row=0, column=0, columnspan=4)
        # set focus to label so that keyboard events are captured
        self.label.focus_set()

        # Create the buttons
        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
            ("C", 5, 0),  # Clear button
            ("√", 5, 1),  # Square root
            ("ln", 5, 2),  # Natural logarithm
            ("sin", 5, 3),  # Sine
        ]

        for button in buttons:
            text, row, col = button
            tk.Button(
                self.root,
                text=text,
                width=7,
                height=2,
                font=custom_font,
                bg='green',
                fg='green',
                command=lambda t=text: self.on_button_click(t),
            ).grid(row=row, column=col)

        # Create a history list
        self.history = []

        # Add a button to clear the history
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

        # Add a button to show the history
        tk.Button(
            self.root,
            text="Show History",
            width=15,
            height=2,
            font=custom_font,
            bg='black',
            fg='green',
            command=self.show_history,
        ).grid(row=6, column=2, columnspan=2)

        # Start the main loop
        self.root.mainloop()

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.label['text'][-1])
                self.history.append(self.label['text'][-1])
                self.label.config(text=str(result))
            except ZeroDivisionError:
                self.label.config(text="Error: Zero Division")
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
        text = ""
        for calc in self.history:
            text += calc + "\n"
        self.label.config(text=text)


if __name__ == "__main__":
    app = CalculatorApp()
