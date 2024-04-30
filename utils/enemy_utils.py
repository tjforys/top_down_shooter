from typing import List

from constants import Constants
from objects.bullet import Bullet
from objects.enemy import Enemy, BlackAmogus, Goku, Pasterz
from objects.player import Player
import time
import random



class EnemyUtils:
    @classmethod
    def handle_enemies(cls, enemies: List[Enemy], player: Player, bullets: List[Bullet]):
        for enemy in enemies:
            cls.move_enemy(enemy, player)
            cls.deal_dmg_to_enemy(enemy, bullets)

        enemies = cls.delete_dead_enemies(enemies)
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
            enemytype = random.choice([1, 2, 3])
            if enemytype == 1:
                enemies.append(BlackAmogus(spawn_coords[0], spawn_coords[1]))
            if enemytype == 2:
                enemies.append(Goku(spawn_coords[0], spawn_coords[1]))
            if enemytype == 3:
                enemies.append(Pasterz(spawn_coords[0], spawn_coords[1]))
            enemy_spawn_time = time.time()
        return enemy_spawn_time, enemies
    
    @staticmethod
    def play_enemy_sounds(enemies: List[Enemy]):
        for enemy in enemies:
            enemy.play_random_sound()


    @staticmethod
    def shoot_bullets(enemies: List[Enemy], enemy_bullets: List[Bullet], player: Player):
        for enemy in enemies:
            if type(enemy) in Constants.shooting_enemy_types:
                enemy_bullets = enemy.shoot(player, enemy_bullets)
        return enemy_bullets
