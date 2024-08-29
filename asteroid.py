import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen, color=(255, 255, 255), center=self.position, radius=self.radius, width=2
        )

    def update(self, delta_time):
        self.position += self.velocity * delta_time
