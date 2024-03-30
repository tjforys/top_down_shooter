from typing import List

import pygame
import time

from classes.file_paths import FilePaths
from objects.music import Music
from objects.bullet import Bullet
from objects.gif_background import BackgroundGIF
from objects.player import Player
from objects.screen import Screen

from classes.draw import Draw


def main():
    running = True

    bg_music = Music(target_file=FilePaths.mp3_monday, volume=0.1, loop=True)
    bg_music.play()

    screen = Screen(screen_x=1000, screen_y=1000)
    background_gif = BackgroundGIF(gif_frames_folder=FilePaths.gif_monday_2, draw_frequency_in_ms=75)

    amongus = pygame.image.load(FilePaths.png_amogus).convert_alpha()
    amongus = pygame.transform.scale(amongus, (40, 52))

    player = Player(sprite=amongus, position=[250, 250], radius=10, speed=1)
    bullets: List[Bullet] = []
    while running:

        screen.fill_screen((255, 255, 255))
        game_time_in_ms = pygame.time.get_ticks()

        Draw.draw_background_gif_pic(screen, background_gif)
        screen.show_current_time(game_time_in_ms)
        player.move(screen.x, screen.y)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                bullets.append(Bullet(pos_x=player.position[0], pos_y=player.position[1], dest_x=mouse_x, dest_y=mouse_y, speed=1))

            if event.type == pygame.QUIT:
                running = False

        for bullet in bullets:
            print(bullet)
            pygame.draw.circle(screen.screen, (0, 0, 0), (bullet.position[0], bullet.position[1]), 40)
            bullet.move()
        bullets = list(filter(lambda b: b.is_in_bounds(screen.x, screen.y), bullets))
        if not bullets:
            print("no more boolets")
 
        Draw.draw_player(screen.screen, player)
        # Draw a solid blue circle in the center
        pygame.display.flip()
        time.sleep(0.001)    

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    main()
