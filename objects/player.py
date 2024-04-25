import pygame
import time
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
        self.rect = pygame.Rect(self.x, self.y, self.hitbox_x, self.hitbox_y)
        self.i_frame_time = 0
        self.i_frames = 1
        self.alive = True

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

        self.x, self.y = Movement.put_back_in_arena_if_outside(area_x, area_y, self.x, self.y)
        self.rect = pygame.Rect(self.x - self.hitbox_x/2, self.y - self.hitbox_y/2, self.hitbox_x, self.hitbox_y)


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

        self.x, self.y = Movement.put_back_in_arena_if_outside(area_x, area_y, self.x, self.y)

    def take_damage(self, screen):
        if time.time() - self.i_frame_time > self.i_frames:
            self.health -= 1
            self.i_frame_time = time.time()
            if self.health < 1:
                screen.show_game_over()
            