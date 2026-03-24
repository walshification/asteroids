import pygame

from asteroids.constants import LINE_WIDTH
from asteroids.entities.circleshape import CircleShape


class Shot(CircleShape):
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
