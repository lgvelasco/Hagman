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

        im = Image.open("JPEG/" + str(self.stage))
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
                print("You already guessed that letter")
            elif a.lower() not in self.bank:
                self.bank.append(a)
                if a.lower() in self.word:
                    for i in self.word:
                        if a == i:
                            self.guessed += 1
                    print("You have guessed a letter")
                    print(self.guessed)
                    print((len(self.word)))
                else:
                    print("Letter not in word")
                    self.stage += 1
                    if self.stage == 6:
                        print("You lose")
                        break

