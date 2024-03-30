import pygame

from objects.gif_background import BackgroundGIF
from objects.player import Player
from objects.screen import Screen

from classes.direction_enums import Directions


class Draw:
    @staticmethod
    def draw_player(screen, player: Player):
        if player.rotation is Directions.RIGHT:
            screen.blit(player.sprite, (player.position[0]-25, player.position[1]-25))
        if player.rotation is Directions.LEFT:
            screen.blit(pygame.transform.flip(player.sprite, True, False), (player.position[0]-25, player.position[1]-25))


    @staticmethod
    def draw_background_gif_pic(screen: Screen, gif: BackgroundGIF):
        last_draw_time_to_update = False
        game_time_in_ms = pygame.time.get_ticks()

        if game_time_in_ms - gif.last_draw_time_in_ms > gif.draw_frequency_in_ms:
            gif.current_frame += 1
            last_draw_time_to_update = True

        pic_to_draw = gif.frames_list[gif.current_frame % len(gif.frames_list)]
        cat = pygame.image.load(f"{gif.frames_folder}\{pic_to_draw}").convert()
        cat = pygame.transform.scale(cat, (screen.x, screen.y))
        screen.screen.blit(cat, (0, 0))

        if last_draw_time_to_update:
            gif.last_draw_time_in_ms = pygame.time.get_ticks()




