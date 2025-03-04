import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SPLIT_ACCELERATION_FACTOR

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255, 0.8), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        pos_vector = self.velocity.rotate(angle)
        neg_vector = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = pos_vector * SPLIT_ACCELERATION_FACTOR
        asteroid2.velocity = neg_vector * SPLIT_ACCELERATION_FACTOR
