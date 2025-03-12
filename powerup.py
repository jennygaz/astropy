import pygame
import random
from constants import POWERUP_TYPES, POWERUP_EFFECT_DURATION

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, powerup_type):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.type = powerup_type
        self.radius = 15

    def draw(self, screen):
        color = (0, 255, 0) if self.type == 'fire_rate' else (255, 0, 0)
        pygame.draw.circle(screen, color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def apply_effect(self, player):
        if self.type == 'fire_rate':
            player.fire_rate *= 0.5
        elif self.type == 'damage':
            player.damage *= 2
        pygame.time.set_timer(pygame.USEREVENT, int(POWERUP_EFFECT_DURATION * 1000))
