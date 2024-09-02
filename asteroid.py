import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color=(255, 255, 255),
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()  # always destroy current asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:  # too small; don't split
            return

        random_angle = random.uniform(20.0, 50.0)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1 * 1.2

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_velocity2 * 1.2
