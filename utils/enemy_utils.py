from typing import List

from objects.bullet import Bullet
from objects.enemy import Enemy
from objects.player import Player


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
        return enemy.move(player.position[0], player.position[1])


    @staticmethod
    def delete_dead_enemies(enemies: List[Enemy]) -> List[Enemy]:
        return list(filter(lambda e: e.health > 0, enemies))
