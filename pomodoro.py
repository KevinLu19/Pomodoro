# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 11/18/19
# File: pomodoro.py
# Purpose: Main file for pomodoro project.
# Modification: N/A
# ----------------------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # Naming the window.
        master.title("Pomodo")
        # Prefix for the window size
        master.geometry("500x400")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        # Reset button 
        # Start button 
        # Quit button 
        # Sessession Numbers

    def say_hi(self):
        print("hi there, everyone!")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()