from typing import List

import pygame

from classes.file_paths import FilePaths
from constants import Constants
from objects.bullet import Bullet
from objects.enemy import Enemy, BlackAmogus, Goku, Pasterz, Michael
from objects.player import Player
import time
import random

from utils.movement_utils import Movement


class EnemyUtils:
    @classmethod
    def handle_enemies(cls, screen, enemies: List[Enemy], player: Player, bullets: List[Bullet]):
        for enemy in enemies:
            cls.move_enemy(enemy, player)
            cls.deal_dmg_to_enemy(enemy, bullets)

            if type(enemy) in [Michael]:
                if not enemy.was_seen and Movement.is_inside_arena(screen.x, screen.y, enemy.x, enemy.y):
                    enemy.music_list[0].play()
                    enemy.was_seen = True
        enemies = cls.delete_dead_enemies(enemies)
        return enemies

    @staticmethod
    def manage_enemy_collision(screen, player: Player, enemies: List[Enemy]):
        if player.rect.collideobjects([enemy.rect for enemy in enemies]):
            player.take_damage()

        for enemy in enemies:
            if type(enemy) == Michael:
                if player.rect.colliderect(enemy.rect):
                    player.take_damage()
                    player.take_damage()
                    player.take_damage()
                    sprite = pygame.image.load(FilePaths.png_explosion).convert_alpha()
                    sprite = pygame.transform.scale(sprite, (250, 150))
                    screen.screen.blit(sprite, (player.x-player.hitbox_x/2-100, player.y-player.hitbox_y/2-80))
                    pygame.display.flip()
                    time.sleep(0.5)
                    enemies.remove(enemy)
        return enemies



    @staticmethod
    def deal_dmg_to_enemy(enemy: Enemy, bullets: List[Bullet]) -> Enemy:
        for bullet in reversed(bullets):
            if enemy.is_hit(bullet):
                enemy.take_damage(1)
        return enemy


    @staticmethod
    def move_enemy(enemy: Enemy, player: Player) -> Enemy:
        return enemy.move(player.x, player.y)


    @staticmethod
    def delete_dead_enemies(enemies: List[Enemy]) -> List[Enemy]:
        return list(filter(lambda e: e.health > 0, enemies))
    
    @staticmethod
    def generate_enemies(enemy_spawn_cd: float, enemy_spawn_location_list: List[tuple], enemy_spawn_time: float, enemies: List[Enemy]):
        if time.time() - enemy_spawn_time > enemy_spawn_cd:
            spawn_coords = random.choice(enemy_spawn_location_list)
            enemytype = random.choice([1, 2, 3, 4])
            if enemytype == 1:
                enemies.append(BlackAmogus(spawn_coords[0], spawn_coords[1]))
            if enemytype == 2:
                enemies.append(Goku(spawn_coords[0], spawn_coords[1]))
            if enemytype == 3:
                enemies.append(Pasterz(spawn_coords[0], spawn_coords[1]))
            if enemytype == 4:
                enemies.append(Michael(spawn_coords[0], spawn_coords[1]))
            enemy_spawn_time = time.time()
        return enemy_spawn_time, enemies
    
    @staticmethod
    def play_enemy_sounds(enemies: List[Enemy]):
        for enemy in enemies:
            if type(enemy) in [Michael]:
                continue
            enemy.play_random_sound()


    @staticmethod
    def shoot_bullets(enemies: List[Enemy], enemy_bullets: List[Bullet], player: Player):
        for enemy in enemies:
            if type(enemy) in [Pasterz]:
                enemy_bullets = enemy.shoot(player, enemy_bullets)
        return enemy_bullets
