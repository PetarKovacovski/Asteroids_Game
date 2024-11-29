from constants import *
import pygame
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
        
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        
        child1 = Asteroid(self.position.x, self.position.y, new_rad)
        child1.velocity = self.velocity.copy().rotate(angle) * 1.2
        
        child2 = Asteroid(self.position.x, self.position.y, new_rad)
        child2.velocity = self.velocity.copy().rotate(-angle) * 1.2
        
        
