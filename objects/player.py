import pygame


class Player():
    def __init__(self, position: list, radius: int, speed: float):
        self.position = position
        self.radius = radius
        self._speed = speed

    
    def move(self, area_x, area_y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.position[0] > 0:
            self.position[0] -= self._speed
        if keys[pygame.K_w] and self.position[1] > 0:
            self.position[1] -= self._speed
        if keys[pygame.K_s] and self.position[1] < area_y:
            self.position[1] += self._speed
        if keys[pygame.K_d] and self.position[0] < area_x:
            self.position[0] += self._speed
            