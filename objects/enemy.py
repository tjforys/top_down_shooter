import math

import pygame
import random
from classes.file_paths import FilePaths
from objects.bullet import Bullet
from objects.music import Music
import time

class Enemy:
    def __init__(self, sprite, pos_x: int, pos_y: int, speed: float, health: int, hitbox: tuple, music_list: list[Music], musicCD: float):
        self.sprite = sprite
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.health = health
        self.hitbox = hitbox
        self.music_list = music_list
        self.last_music_time = 0
        self.musicCD = musicCD


    def move(self, player_x: int, player_y: int):
        whole_distance = math.dist((self.pos_x, self.pos_y), (player_x, player_y))
        distance_x = player_x - self.pos_x
        distance_y = player_y - self.pos_y

        speed_x = self.speed*distance_x/whole_distance
        speed_y = self.speed*distance_y/whole_distance
        #cos zrobic jak sie nachodza bo wtedy crashuje bo dzieilisz przez 0

        self.pos_x += speed_x
        self.pos_y += speed_y


    def is_hit(self, bullet: Bullet):
        if bullet.position[0] - bullet.radius < self.pos_x + self.hitbox[0] and bullet.position[0] + bullet.radius > self.pos_x:
            if bullet.position[1] - bullet.radius < self.pos_y + self.hitbox[1] and bullet.position[1] + bullet.radius > self.pos_y:
                return True          
        return False
    

    def play_random_sound(self):
        if time.time() - self.last_music_time > self.musicCD:
            random.choice(self.music_list).play()
            self.last_music_time = time.time()


    def take_damage(self, amount: float):
        self.health -= amount
        if self.health < 1:
            del self


class BlackAmogus(Enemy):
    def __init__(self, pos_x, pos_y):
        black_impostor = pygame.image.load(FilePaths.png_enemy_sprite_black_impostor).convert_alpha()
        black_impostor = pygame.transform.scale(black_impostor, (40, 52))

        super().__init__(
            sprite=black_impostor,
            health=10,
            pos_x=pos_x,
            pos_y=pos_y,
            speed=0.5,
            hitbox=(20, 40),
            music_list=[Music(target_file=FilePaths.mp3_black_impostor)],
            musicCD=5
        )


class Goku(Enemy):
    def __init__(self, pos_x, pos_y):
        goku = pygame.image.load(FilePaths.png_goku).convert_alpha()
        goku = pygame.transform.scale(goku, (60, 75))
        super().__init__(
            sprite=goku,
            health=5e0,
            pos_x=pos_x,
            pos_y=pos_y,
            speed=1,
            hitbox=(30, 60),
            music_list=[Music(target_file=FilePaths.mp3_goku1, volume=0.2), Music(target_file=FilePaths.mp3_goku2, volume= 0.2), Music(FilePaths.mp3_goku3, volume=0.2)],
            musicCD=5
        )