import pygame
from shot import Shot

class SpecialShot(Shot):
    def __init__(self, x, y, damage):
        super().__init__(x, y)
        self.damage = damage

    def update(self, dt):
        self.position += self.velocity * dt
        # Additional behavior for special shots can be added here
