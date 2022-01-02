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
        self.WIDTH = self.screen.get_size()[0]
        self.HEIGHT = self.screen.get_size()[1]
        self.font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 22)
        self.streams = []
        # DOWN for TRILOGY, UP for RESURRECTIONS
        self.direction = "DOWN"

    def main_loop(self):

        while True:

            # Add a new stream if not too many...
            if len(self.streams) < STREAM_MAX and random.random() < STREAM_GEN:
                stream = Stream(self.screen, self.font, self.direction)
                self.streams.append(stream)

            self._handle_input()
            self._process_game_logic()
            self._draw()
            self.streams = [s for s in self.streams if s.visible]  # only keep the visible ones

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Matrix")
        pygame.font.init()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.direction == "DOWN":
                    self.direction = "UP"
                else:
                    self.direction = "DOWN"

    def _process_game_logic(self):
        for s in self.streams:
            s.move()

    def _draw(self):
        self.screen.fill((0, 0, 0))
        text = self.font.render("<Press ESC to exit; Mouse Click to RESURRECT!>", False, (75, 150, 75))
        textrect = text.get_rect(center=(self.WIDTH / 2, self.HEIGHT - 11))
        self.screen.blit(text, textrect)
        for s in self.streams:
            s.draw()
        pygame.display.flip()
