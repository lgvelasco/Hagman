import random

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

