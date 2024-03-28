# Simple pygame program

# Import and initialize the pygame library
import pygame
import time

from objects.bullet import Bullet
from objects.player import Player

pygame.init()
screen_x, screen_y = 1000, 1000
# Set up the drawing window
screen = pygame.display.set_mode([screen_x, screen_y])

# Run until the user asks to quit
running = True

player = Player(position=[250, 250], radius=75, speed=1)
bullets: list[Bullet] = []
while running:
    player.move()

    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullets.append(Bullet(pos_x=player.position[0], pos_y=player.position[1], dest_x=mouse_x, dest_y=mouse_y, speed=1))

        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    for bullet in bullets:
        print(bullet)
        pygame.draw.circle(screen, (0, 0, 0), (bullet.position[0], bullet.position[1]), 10)
        bullet.move()
    bullets = list(filter(lambda b: b.is_in_bounds(screen_x, screen_y), bullets))
    # Fill the background with white
    if not bullets:
        print("no more boolets")

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), player.position, player.radius)

    # Flip the display
    pygame.display.flip()
    time.sleep(0.001)    
# Done! Time to qui3.
pygame.quit()


# if __name__ == "__main__":
