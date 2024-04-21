import pygame

from classes.direction_enums import Directions
from classes.file_paths import FilePaths
from utils.movement_utils import Movement


class Player:
    def __init__(self, position: list, radius: int, speed: float, hitbox: tuple, max_hp: int):
        self.hitbox = hitbox
        amongus = pygame.image.load(FilePaths.png_amogus).convert_alpha()
        amongus = pygame.transform.scale(amongus, (self.hitbox[0], self.hitbox[1]))

        self.sprite = amongus
        self.rotation = Directions.RIGHT
        self.position = position
        self.radius = radius
        self.max_hp = max_hp
        self.current_hp = max_hp
        self._speed = speed
        

    
    def move(self, area_x, area_y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.position[0] -= self._speed
            self.rotation = Directions.LEFT

        if keys[pygame.K_w]:
            self.position[1] -= self._speed

        if keys[pygame.K_s]:
            self.position[1] += self._speed

        if keys[pygame.K_d]:
            self.position[0] += self._speed
            self.rotation = Directions.RIGHT

        self.position = Movement.put_back_in_arena_if_outside(area_x, area_y, self.position)


    def dash(self, dash_distance, area_x, area_y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.position[0] -= dash_distance
        if keys[pygame.K_w]:
            self.position[1] -= dash_distance
        if keys[pygame.K_d]:
            self.position[0] += dash_distance
        if keys[pygame.K_s]:
            self.position[1] += dash_distance

        self.position = Movement.put_back_in_arena_if_outside(area_x, area_y, self.position)
            