from constants import *
import pygame
from circleshape import CircleShape
import random



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("killing ", self.radius)
            return
        else:
            print("splitting ", self.radius)
            angle_to_split=random.uniform(20,50)
            v1 = self.velocity.rotate(angle_to_split)
            v2 = self.velocity.rotate(-angle_to_split)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = v1 * 1.2
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2.velocity = v2 * 1.2


