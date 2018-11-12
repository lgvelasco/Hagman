from tkinter import *


class GUI:
    def __init__(self, window):
        self.window = window
        bgcolor = "#20207f"
        title = "Hangman Game"
        window.title("Hangman")
        window.geometry("1400x700")
        window.resizable(0, 0)

        self.frame = Frame(master=window, bg=bgcolor)
        self.frame.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
        self.frame.pack(fill=BOTH, expand=1)  # Expand the frame to fill the root window

        # Create a canvas to display the cards on
        self.image_frame = Frame(master=self.frame)
        self.canvas = []
        for i in range(5):
            # set the background to green to simulate a table and set the border thickness to 0
            self.canvas.append(Canvas(master=self.image_frame, width=250, height=500, bg="green", highlightthickness=0))
            self.canvas[i].grid(row=0, column=i)

        self.image_frame.grid(row=1, padx=20)

        self.label = Label(self.frame, text="", bg=bgcolor, fg="white")
        self.label.grid(row=5)
        self.label.config(font=("Courier", 44))
        self.label2 = Label(self.frame, text=title, bg=bgcolor, fg="White")
        self.label2.grid(row=0, columnspan=2)
        self.label2.config(font=("Courier", 20))

        self.bt1 = Button(self.frame, text="Hit me!")
        self.bt1.config(font=("Courier", 15))
        self.bt1.grid(row=1, column=1, columnspan=2)
        self.bt2 = Button(self.frame, text="Exit Game", bg="black", fg="yellow")
        self.bt2.grid(row=2, column=2)


window = Tk(screenName="Hangman")
hangman_game = GUI(window)
window.mainloop()