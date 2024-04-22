import pygame

from classes.direction_enums import Directions
from classes.file_paths import FilePaths
from utils.movement_utils import Movement


class Player:
    def __init__(self, x: int, y: int, radius: int, speed: float, hitbox_x: int, hitbox_y, max_hp: int):
        self.rotation = Directions.RIGHT
        self.x = x
        self.y = y
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y
        self.radius = radius
        self.max_hp = max_hp
        self.health = max_hp
        self._speed = speed

        amongus = pygame.image.load(FilePaths.png_amogus).convert_alpha()
        amongus = pygame.transform.scale(amongus, (self.hitbox_x, self.hitbox_y))
        self.sprite = amongus

    
    def move(self, area_x, area_y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self._speed
            self.rotation = Directions.LEFT

        if keys[pygame.K_w]:
            self.y -= self._speed

        if keys[pygame.K_s]:
            self.y += self._speed

        if keys[pygame.K_d]:
            self.x += self._speed
            self.rotation = Directions.RIGHT

        self.position = Movement.put_back_in_arena_if_outside(area_x, area_y, self.x, self.y)


    def dash(self, dash_distance, area_x, area_y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= dash_distance
        if keys[pygame.K_w]:
            self.y -= dash_distance
        if keys[pygame.K_d]:
            self.x += dash_distance
        if keys[pygame.K_s]:
            self.y += dash_distance

        self.position = Movement.put_back_in_arena_if_outside(area_x, area_y, self.x, self.y)
            