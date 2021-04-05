# SYMBOL- a single drop of rain

import random

# Counter determines how quickly a symbol changes
COUNTER_MAX = 50
COUNTER_MIN = 20


def check_range(col):
    if col > 255:
        col=255
    if col < 0:
        col = 0
    return col


class Symbol:
    def __init__(self, screen, font, num, x, y, v):
        self.screen = screen    # screen to draw to
        self.font = font      # font to draw with
        self.num = num      # position in the stream
        self.Y = y          # Position across the screen (left=0)
        self.X = x          # Altitude (top=0)
        self.velocity = v   # velocity - decrement in height
        self.counter = 0
        self.symbol = ""
        self.reset()    # setup the symbol and change counter
        self.colour = self.set_color()

    def move(self):
        self.X += self.velocity
        self.counter -= 1
        if self.counter <= 0:
            self.reset()

    def draw(self):
        text = self.font.render(self.symbol, False, self.colour)
        textrect = text.get_rect(center=(self.Y, self.X))
        self.screen.blit(text, textrect)

    def visible(self, max_height):
        return self.X < max_height

    def reset(self):
        c = random.randint(0, 20)
        if c < 1:
            self.symbol = chr(0x0391 + round(random.randint(0, 26)))  # Greek unicode block
        elif c < 3:
            self.symbol = chr(0x2F00 + round(random.randint(0, 96)))  # Kangxi unicode block
        elif c < 5:
            self.symbol = chr(0x0401 + round(random.randint(0, 26)))  # Cyrillic unicode block
        else:
            self.symbol = chr(0x30A0 + round(random.randint(0, 96)))  # katakana unicode block
        self.counter = random.randint(COUNTER_MIN, COUNTER_MAX)  # countdown timer used to switch symbol

    def set_color(self):
        seed = random.randint(0, 30)
        if self.num == 1:
            r = g = b = 255 - seed
        else:
            r = b = check_range(seed * self.num/10)
            g = check_range(255 - (random.randint(self.num, self.num * 5)))
        return r, g, b
