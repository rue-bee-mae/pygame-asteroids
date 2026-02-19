from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

import pygame
import random

from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        split_angle = random.uniform(20, 50)
        angle_one = self.velocity.rotate(split_angle)
        angle_two = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_one.velocity = angle_one * 1.2
        asteroid_two.velocity = angle_two * 1.2
