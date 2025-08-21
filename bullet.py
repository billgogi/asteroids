from circleshape import CircleShape
import constants
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.velocity = velocity
        if Shot.containers:
            for group in Shot.containers:
                group.add(self)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (int(self.position.x), int(self.position.y)), self.radius)