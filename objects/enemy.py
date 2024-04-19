import math

import pygame
import random
from classes.file_paths import FilePaths
from objects.bullet import Bullet
from objects.music import Music
import time

class Enemy:
    def __init__(self, pos_x: int, pos_y: int, speed: float, health: int, hitbox: tuple, music_list: list[Music], musicCD: float):
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
        if whole_distance == 0: 
            whole_distance = 1
        distance_x = player_x - self.pos_x
        distance_y = player_y - self.pos_y

        speed_x = self.speed*distance_x/whole_distance
        speed_y = self.speed*distance_y/whole_distance

        self.pos_x += speed_x
        self.pos_y += speed_y


    def is_hit(self, bullet: Bullet):
        if bullet.position[0] - bullet.radius + self.hitbox[0]/2 < self.pos_x + self.hitbox[0] and bullet.position[0] + self.hitbox[0]/2 + bullet.radius > self.pos_x:
            if bullet.position[1] - bullet.radius + self.hitbox[1]/2 < self.pos_y + self.hitbox[1] and bullet.position[1] + self.hitbox[1]/2 + bullet.radius > self.pos_y:
                return True          
        return False
    

    def play_random_sound(self):
        if time.time() - self.last_music_time > self.musicCD:
            random.choice(self.music_list).play()
            self.last_music_time = time.time()


    def take_damage(self, amount: float):
        self.health -= amount
        if self.health < 1:
            Music(FilePaths.mp3_enemy_death, volume= 0.3).play()
            del self


class BlackAmogus(Enemy):
    def __init__(self, pos_x, pos_y):
        # black_impostor = pygame.image.load(FilePaths.png_enemy_sprite_black_impostor).convert_alpha()
        # black_impostor = pygame.transform.scale(black_impostor, (40, 52))

        super().__init__(
            health=10,
            pos_x=pos_x,
            pos_y=pos_y,
            speed=0.5,
            hitbox=(30, 30*1.1875),
            music_list=[Music(target_file=FilePaths.mp3_black_impostor, volume=0.05)],
            musicCD=5
        )
        black_impostor = pygame.image.load(FilePaths.png_enemy_sprite_black_impostor).convert_alpha()
        black_impostor = pygame.transform.scale(black_impostor, (self.hitbox[0], self.hitbox[1]))
        self.sprite = black_impostor



class Goku(Enemy):
    def __init__(self, pos_x, pos_y):       
        super().__init__(
            health=5,
            pos_x=pos_x,
            pos_y=pos_y,
            speed=1,
            hitbox=(40, 40*3.154),
            music_list=[Music(target_file=FilePaths.mp3_goku1, volume=0.2), Music(target_file=FilePaths.mp3_goku2, volume= 0.2), Music(FilePaths.mp3_goku3, volume=0.2)],
            musicCD=5
        )
        goku = pygame.image.load(FilePaths.png_goku).convert_alpha()
        goku = pygame.transform.scale(goku, (self.hitbox[0], self.hitbox[1]))
        self.sprite = goku