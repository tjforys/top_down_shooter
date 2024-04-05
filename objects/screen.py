import pygame

from classes.colors import Color


class Screen:
    def __init__(self, screen_x, screen_y):
        self.x = screen_x
        self.y = screen_y
        self.screen = self._initialize_screen()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    
    def _initialize_screen(self):
        return pygame.display.set_mode([self.x, self.y])
    

    def show_current_time(self, current_time_in_ms: int) -> None:
        text_surface = self.font.render(f'{current_time_in_ms/1000}s', False, Color.white)
        text_rect = text_surface.get_rect(center=(self.x/2, 15))
        self.screen.blit(text_surface, text_rect)

    
    def fill_screen(self, color: tuple):
        self.screen.fill(color)    
