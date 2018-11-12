import random
from tkinter import *

from PIL import ImageTk, Image


class Words(object):
    def __init__(self, txt):
        self.words = []
        f = open(txt, "r")
        for line in f:
            self.words.append(line.lower())

    def pick_word(self):
        r = random.randint(0, len(self.words))
        return self.words[r]

    def print(self):
        for i in range(0, len(self.words)):
            print(self.words[i])



class Game(object):
    def __init__(self):
        self.bank = []
        self.guessed = 0
        self.words = Words("available_words.txt")
        self.word = self.words.pick_word()
        self.split_word = list(self.word)

        self.stage = 0

    def print_canvas(self, canvas):
        size = 400, 1000
        stage_name = str(self.stage) + ".jpg"
        im = Image.open("JPEG/" + str(stage_name))
        im.thumbnail(size)
        canvas.image = ImageTk.PhotoImage(im)
        canvas.create_image(40, 160, image=canvas.image, anchor="nw")

    def continue_game(self):
        if self.guessed + 1 == len(self.word):
            return False
        else:
            print("You have won")
            return True

    def guess(self):
        print(self.word)
        while self.continue_game():
            a = input("Please enter a letter: ")
            if a.lower() in self.bank:
                return "You already guessed that letter"
            elif a.lower() not in self.bank:
                self.bank.append(a)
                if a.lower() in self.word:
                    for i in self.word:
                        if a == i:
                            self.guessed += 1
                    return "You have guessed a letter"
                else:
                    return "Letter not in word"
                    self.stage += 1
                    if self.stage == 6:
                        return "You lose"
                        break


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

        self.bt1 = Button(self.frame, text="Start Game!", command=self.start_game())
        self.bt1.config(font=("Courier", 15))
        self.bt1.grid(row=1, column=1, columnspan=2)
        self.bt2 = Button(self.frame, text="Exit Game", bg="black", fg="yellow")
        self.bt2.grid(row=2, column=2)

    def start_game(self):
        game = Game()
        game.guess()
        self.label.config(text=game.word)
        game.print_canvas(self.canvas)

    def exit_game(self):
        exit(0)


window = Tk(screenName="Hangman")
hangman_game = GUI(window)
window.mainloop()
