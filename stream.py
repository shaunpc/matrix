# STREAM- a stream of raindrops

import random
from symbol import Symbol

# VELOCITY determines the speed of a stream
VEL_MIN = 50
VEL_MAX = 80
VEL_DIV = 10

# LENGTH determines the number of symbols in a single stream
LEN_MIN = 25
LEN_MAX = 50


class Stream:
    def __init__(self, screen, font):
        self.screen = screen    # screen to draw to
        self.font = font      # font to draw with
        self.WIDTH = self.screen.get_size()[0]
        self.HEIGHT = self.screen.get_size()[1]
        self.visible = True

        # Obtain random start position across width of screen
        self.Y = random.randint(0, self.WIDTH)
        self.velocity = random.randint(VEL_MIN, VEL_MAX) / VEL_DIV          # speed at which the rain drops

        # Obtain random length of stream
        self.symbols = []
        linesize = self.font.get_linesize()
        for i in range(1, random.randint(LEN_MIN, LEN_MAX)):
            x_pos = 0 - (i*linesize)
            self.symbols.append(Symbol(self.screen, self.font, i, x_pos, self.Y, self.velocity))

    def move(self):
        self.visible = False
        for s in self.symbols:
            s.move()
            self.visible = (self.visible | s.visible(self.HEIGHT))

    def draw(self):
        for s in self.symbols:
            s.draw()

    def visible(self, max_height):
        return self.visible
