import pygame

from objects.player import Player

from classes.direction_enums import Directions


class Draw:
    @staticmethod
    def draw_player(screen, player: Player):
        if player.rotation is Directions.RIGHT:
            screen.blit(player.sprite, (player.position[0]-25, player.position[1]-25))
        if player.rotation is Directions.LEFT:
            screen.blit(pygame.transform.flip(player.sprite, True, False), (player.position[0]-25, player.position[1]-25))
