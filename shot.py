import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Shot(CircleShape):
        def __init__(self, x, y, radius, player):
            super().__init__(x, y, radius)
            self.x = 9
            self.y = 9
            self.radius = radius
            val1 = player.position[0]
            val2 = player.position[1]
            self.position = pygame.Vector2(val1, val2)
            

        def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

        def update(self, dt):
            self.position += (self.velocity * dt)