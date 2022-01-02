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
    def __init__(self, screen, font, direction):
        self.screen = screen    # screen to draw to
        self.font = font      # font to draw with
        self.WIDTH = self.screen.get_size()[0]
        self.visible = True
        self.Y = random.randint(0, self.WIDTH)  # Obtain random start position across width of screen

        # which way stream flows - "UP" or "DOWN" screen...
        if direction == "DOWN":
            self.START_HEIGHT = 0                           # start = top
            self.END_HEIGHT = self.screen.get_size()[1]     # end   = bottom
            self.velocity = random.randint(VEL_MIN, VEL_MAX) / VEL_DIV  # speed at which the rain drops
        else:
            self.START_HEIGHT = self.screen.get_size()[1]   # start = bottom
            self.END_HEIGHT = 0                             # end   = top
            self.velocity = - random.randint(VEL_MIN, VEL_MAX) / VEL_DIV  # speed at which the rain rises

        # Obtain random length of stream
        self.symbols = []
        linesize = self.font.get_linesize()
        for i in range(1, random.randint(LEN_MIN, LEN_MAX)):
            if direction == "DOWN":
                x_pos = self.START_HEIGHT - ((i-1) * linesize)  # start positions above
            else:
                x_pos = self.START_HEIGHT + ((i-1) * linesize)  # start positions below
            self.symbols.append(Symbol(self.screen, self.font, i, x_pos, self.Y, self.velocity))

    def move(self):
        self.visible = False
        for s in self.symbols:
            s.move()
            # print(self.START_HEIGHT, self.END_HEIGHT, s.X, s.visible(self.START_HEIGHT, self.END_HEIGHT))
            self.visible = (self.visible | s.visible(self.START_HEIGHT, self.END_HEIGHT))
        # print(self, self.visible)

    def draw(self):
        for s in self.symbols:
            s.draw()

    def visible(self):
        return self.visible
