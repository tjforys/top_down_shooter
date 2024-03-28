import pygame


class Player():
    def __init__(self, position: list, radius: int, speed: float):
        self.position = position
        self.radius = radius
        self._speed = speed

    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.position[0] -= self._speed
        if keys[pygame.K_w]:
            self.position[1] -= self._speed
        if keys[pygame.K_s]:
            self.position[1] += self._speed
        if keys[pygame.K_d]:
            self.position[0] += self._speed
            