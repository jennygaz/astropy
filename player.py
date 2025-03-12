import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from shot import Shot
from specialshot import SpecialShot

class Player(CircleShape):
    containers = ()
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.shoot_timer = 0.0
        self.rotation = 0
        self.fire_rate = PLAYER_SHOOT_COOLDOWN
        self.damage = 1
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def shoot(self):
        if self.shoot_timer > 0:
            return
        shot = SpecialShot(self.position.x, self.position.y, self.damage)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_timer = self.fire_rate

    def apply_powerup(self, powerup_type):
        if powerup_type == 'fire_rate':
            self.fire_rate *= 0.5
        elif powerup_type == 'damage':
            self.damage *= 2
