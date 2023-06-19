"""
Application Name: CalApp
Version: 0.1
Created by: Obaid Aldosari
Github: https://github.com/ODosari
"""

import tkinter as tk
import tkinter.font as tkFont


class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator Application")
        self.root.geometry("655x500+500+200")
        self.root.resizable(width=False, height=False)

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

        # Start the main loop
        self.root.mainloop()

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.label['text'])
                self.label.config(text=str(result))
            except ZeroDivisionError:
                self.label.config(text="Error: Zero Division")
        elif text == "C":
            self.label.config(text="")
        else:
            self.label.config(text=self.label['text'] + text)

        # Bind keypress events to label
        self.label.bind("<Key>", self.on_keypress)
        # Bind Enter key to "=" button
        self.label.bind("<Return>", lambda event: self.on_button_click("="))

    def on_keypress(self, event):
        key = event.char
        if key == "\r":  # Handle Enter key
            self.on_button_click("=")
        elif key == "\x08":  # Handle Backspace key
            self.label.config(text=self.label['text'][:-1])
            # Allow only digits and math operators
        elif key.isdigit() or key == "+" or key == "-" or key == "*" or key == "/":
            self.label.config(text=self.label['text'] + key)


if __name__ == "__main__":
    app = CalculatorApp()
