# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 12/3/2019
# File: PomodoroTimer.py
# Purpose: Main file for pomodoro project.
# Modification: - Added more buttons
# ----------------------------------------------------------------------------------------

from tkinter import *

class Window(Frame):
    def __init__ (self, master=None):
        
        # Parameters wanted in Class.
        Frame.__init__(self, master)

        # Makes tk window the master.
        self.master = master

        self.init_window()

    # Creation of init_window
    def init_window(self):
        self.master.title("Pomodoro Timer")

        self.pack(fill=BOTH, expand=1)

        # Creation of quit button. Also call function "client_exit"
        quitBttn = Button(self, text="Quit", command=self.client_exit)
        quitBttn.place(x = 10, y = 10)

        # Start Button 
        startBttn = Button(self, text="Start", command=self.start_session)

        # Reset Button
        resetBttn = Button(self, text="Reset", command=self.reset)

        # Session Number

        # Pause Button
        pauseBttn = Button(self, text="Pause", command=self.pause)
        
    def client_exit(self):
        exit()

    def start_session(self):
        pass

    def reset(self):
        pass

    def pause(self):
        pass

if (__name__ == "__main__"):
    root = Tk()
    root.geometry("500x400")
    root.configure(background="black")
    app = Window(root)
    root.mainloop()
