# Simple pygame program

# Import and initialize the pygame library
import pygame
import time
import os
from objects.bullet import Bullet
from objects.player import Player
from objects.screen import Screen

from classes.draw import Draw


def main():
    running = True
    gif_list = os.listdir("sprite/monday/")
    screen = Screen(screen_x=1000, screen_y=1000)

    amongus = pygame.image.load("sprite/image.png").convert_alpha()
    amongus = pygame.transform.scale(amongus, (40, 52))

    player = Player(sprite=amongus, position=[250, 250], radius=10, speed=1)
    bullets: list[Bullet] = []
    current_time = pygame.time.get_ticks()-100
    i=0
    while running:

        screen.fill_screen((255, 255, 255))
        game_time_in_ms = pygame.time.get_ticks()
        
        if game_time_in_ms - current_time > 50:
            next_image = gif_list[i % 180]
            cat = pygame.image.load(f"sprite/monday/{next_image}").convert()
            cat = pygame.transform.scale(cat, (1000, 1000))
            i+=1
            current_time = pygame.time.get_ticks()
        screen.screen.blit(cat, (0, 0))
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