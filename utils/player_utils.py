from objects.player import Player
from objects.enemy import Enemy
from objects.screen import Screen
from typing import List


class PlayerUtils:
    @staticmethod
    def manageEnemyCollision(player: Player, enemies: List[Enemy], screen: Screen):
        if player.rect.collideobjects([enemy.rect for enemy in enemies]):
            player.take_damage()
            if not player.alive:
                screen.show_game_over()