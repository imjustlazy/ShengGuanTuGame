# coding: utf-8

import random

class Dice(object):
    surface = None

    def __init__(self):
        self.surface = 0
    
    def roll(self):
        self.surface = random.randint(1, 6)

    def get(self):
        self.roll()
        return self.surface

class Dices(object):
    dice_a, dice_b, dice_c = None, None, None
    kind = None

    def __init__(self):
        self.dice_a, self.dice_b, self.dice_c = Dice(), Dice(), Dice()
    
    def sort(self):
        a, b, c = self.dice_a.surface, self.dice_b.surface, self.dice_c.surface
        a, b, c = min(a,b,c), sum((a,b,c)) - min(a,b,c) - max(a,b,c), max(a,b,c)
        self.dice_a.surface, self.dice_b.surface, self.dice_c.surface = a, b, c

    def roll(self):
        self.dice_a.roll(); self.dice_b.roll(); self.dice_c.roll()
        self.sort()

    def judge_kind(self):
        a, b, c = self.dice_a.surface, self.dice_b.surface, self.dice_c.surface
        if a == c: # 'baozi' means 3 dices showing the same number
            self.kind = 3
        elif (a, b, c) == (4, 5, 6):
            self.kind = 2
        elif (a, b, c) == (1, 2, 3):
            self.kind = -3
        elif (a, b, c) == (2, 3, 4):
            self.kind = -2
        else:
            self.kind = None
    
    def status(self):
        return self.kind, (self.dice_a.surface, self.dice_b.surface, self.dice_c.surface)
    
    def get(self):
        self.roll()
        self.judge_kind()
        return self.status()
