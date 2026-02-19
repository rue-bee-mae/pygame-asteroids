import pygame


class Score:
    def __init__(self, name, size):
        self.font_name = name
        self.font_size = size
        self.score = 0

    def render(self, text, antialias, color):
        return pygame.font.SysFont(self.font_name, self.font_size).render(str(text), antialias, color)

    def change_score(self, num):
        self.score += num
