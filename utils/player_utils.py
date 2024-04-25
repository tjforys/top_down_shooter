from objects.player import Player
from objects.enemy import Enemy
from objects.screen import Screen
from objects.bullet import Bullet
from typing import List


class PlayerUtils:
    @staticmethod
    def manageEnemyCollision(player: Player, enemies: List[Enemy], screen: Screen):
        if player.rect.collideobjects([enemy.rect for enemy in enemies]):
            player.take_damage(screen=screen)


    @staticmethod
    def manageEnemyBulletsCollistion(player: Player, enemy_bullets: List[Bullet], screen: Screen):
        if player.rect.collideobjects([bullet.rect for bullet in enemy_bullets]):
            player.take_damage(screen=screen)
        return list(filter(lambda b: not b.rect.colliderect(player.rect), enemy_bullets))