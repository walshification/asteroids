import pygame

from asteroids.entities.circleshape import CircleShape
from asteroids.constants import (
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SHOT_RADIUS,
)
from asteroids.entities.shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown_timer = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * (self.radius / 1.5)
        a = self.position + pygame.Vector2(forward * self.radius)
        b = self.position - pygame.Vector2(forward * self.radius) - right
        c = self.position - pygame.Vector2(forward * self.radius) + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def move(self, dt):
        start = pygame.Vector2(0, 1)
        rotated = start.rotate(self.rotation)
        rotated_with_speed = rotated * PLAYER_SPEED * dt
        self.position += rotated_with_speed

    def shoot(self):
        if self.shoot_cooldown_timer > 0:
            return

        self.shoot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot_vector = pygame.Vector2(0, 1)
        rotated = shot_vector.rotate(self.rotation)
        shot_vector_with_speed = rotated * PLAYER_SHOOT_SPEED
        shot.velocity += shot_vector_with_speed

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shoot_cooldown_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
