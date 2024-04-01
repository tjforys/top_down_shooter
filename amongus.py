import pygame
import time


from typing import List

from objects.music import Music
from objects.bullet import Bullet
from objects.gif_background import BackgroundGIF
from objects.player import Player
from objects.screen import Screen
from objects.enemy import Enemy

from classes.draw import Draw
from classes.file_paths import FilePaths


def handle_enemies(screen, enemies: List[Enemy], bullets: List[Bullet], player: Player) -> List[Enemy]:
    for enemy_obj in enemies:
        enemy_obj.move(player.position[0], player.position[1])
        for bullet in reversed(bullets):
            if enemy_obj.is_hit(bullet):
                enemy_obj.take_damage(1)
        Draw.draw_enemy(screen=screen, enemy=enemy_obj)
    return enemies


def delete_hit_bullets(bullets: List[Bullet], enemies: List[Enemy]) -> List[Bullet]:
    return list(filter(lambda b: all([not enemy_obj.is_hit(b) for enemy_obj in enemies]), bullets))


def delete_dead_enemies(enemies: List[Enemy]) -> List[Enemy]:
    return list(filter(lambda e: e.health>0, enemies))


def filter_out_of_bounds_bullets(screen, bullets: List[Bullet]) -> List[Bullet]:
    return list(filter(lambda b: b.is_in_bounds(screen.x, screen.y), bullets))
    

def main():
    running = True

    pygame.mouse.set_visible(False)

    bg_music = Music(target_file=FilePaths.mp3_monday, volume=0.1, loop=True)
    amongus_sfx = Music(target_file="mp3/amongus.mp3", volume= 0.1, loop=False)
    bg_music.play()

    screen = Screen(screen_x=500, screen_y=500)
    background_gif = BackgroundGIF(gif_frames_folder=FilePaths.gif_monday_2, draw_frequency_in_ms=75)

    cursor = pygame.image.load(FilePaths.png_cursor).convert_alpha()
    cursor = pygame.transform.scale(cursor, (32, 32))
    cursor_img_rect = cursor.get_rect()

    amongus = pygame.image.load(FilePaths.png_amogus).convert_alpha()
    amongus = pygame.transform.scale(amongus, (40, 52))

    enemy_sprite = pygame.image.load(FilePaths.png_enemy_sprite_black_impostor).convert_alpha()
    enemy_sprite = pygame.transform.scale(enemy_sprite, (40, 52))
    
    player = Player(sprite=amongus, position=[250, 250], radius=10, speed=1)

    bullets: List[Bullet] = []

    enemies: List[Enemy] = [Enemy(sprite= enemy_sprite, pos_x=1000, pos_y=1000, speed=0.5, health=10),
                            Enemy(sprite= enemy_sprite, pos_x=0, pos_y=0, speed=0.5, health=10)]

    while running:

        screen.fill_screen((255, 255, 255))
        game_time_in_ms = pygame.time.get_ticks()

        Draw.draw_background_gif_pic(screen, background_gif)
        screen.show_current_time(game_time_in_ms)
        Draw.draw_cursor(screen, cursor, cursor_img_rect)
        player.move(screen.x, screen.y)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                amongus_sfx.play()
                bullets.append(Bullet(pos_x=player.position[0], pos_y=player.position[1], dest_x=mouse_x, dest_y=mouse_y, speed=1, radius= 40))

            if event.type == pygame.QUIT:
                running = False

        for bullet in bullets:
            print(bullet)
            pygame.draw.circle(screen.screen, (0, 0, 0), (bullet.position[0], bullet.position[1]), bullet.radius)
            bullet.move()
        bullets = filter_out_of_bounds_bullets(screen=screen, bullets=bullets)
        if not bullets:
            print("no more boolets")
 
        Draw.draw_player(screen.screen, player)
        enemies = handle_enemies(screen=screen,
                                 enemies=enemies,
                                 bullets=bullets,
                                 player=player)

        bullets = delete_hit_bullets(bullets=bullets, enemies=enemies)
        enemies = delete_dead_enemies(enemies=enemies)
        # Draw a solid blue circle in the center
        pygame.display.flip()
        time.sleep(0.001)    

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    main()
