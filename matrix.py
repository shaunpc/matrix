# Matrix Display
#
#

import pygame
import random
from stream import Stream


# DIMENSIONS of screen
WIDTH = 1600
HEIGHT = 1000

# STREAM determines maximum number of streams at any one time, and how frequently to generate
STREAM_MAX = 500
STREAM_GEN = 0.1


class Matrix:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode()  # FullScreen
        self.font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 22)
        self.streams = []

    def main_loop(self):

        while True:

            # Add a new stream if not too many...
            if len(self.streams) < STREAM_MAX and random.random() < STREAM_GEN:
                stream = Stream(self.screen, self.font)
                self.streams.append(stream)

            self._handle_input()
            self._process_game_logic()
            self._draw()
            self.streams = [s for s in self.streams if s.visible]

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Matrix")
        pygame.font.init()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

    def _process_game_logic(self):
        for s in self.streams:
            s.move()

    def _draw(self):
        self.screen.fill((0, 0, 0))
        for s in self.streams:
            s.draw()
        pygame.display.flip()

