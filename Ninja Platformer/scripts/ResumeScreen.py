import pygame, sys

from pygame.locals import *
from scripts.menu import Menu

class Resume:
    def __init__(self):
        self.mainClock = pygame.time.Clock()
        pygame.init()
        self.screen = pygame.display.set_mode((1100, 820), 0, 32)
        self.font = pygame.font.SysFont(None, 70)
        self.main_menu()
        return

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def main_menu(self):
        click = False
        while True:

            self.draw_text('Pause', self.font, (255, 255, 255), self.screen, 50, 90)

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(50, 200, 190, 60)
            button_2 = pygame.Rect(50, 300, 470, 60)
            button_3 = pygame.Rect(50, 400, 100, 60)
            if button_1.collidepoint((mx, my)):
                if click:
                    self.ResumeGame()
                    return
            if button_2.collidepoint((mx, my)):
                if click:
                    self.BackToMenu()
            if button_3.collidepoint((mx, my)):
                if click:
                    self.quit()
            pygame.draw.rect(self.screen, (38, 38, 38), button_1)
            self.draw_text('Resume', self.font, (255, 255, 255), self.screen, 50, 205)
            pygame.draw.rect(self.screen, (38, 38, 38), button_2)
            self.draw_text('Back To Main Menu', self.font, (255, 255, 255), self.screen, 50, 305)
            pygame.draw.rect(self.screen, (38, 38, 38), button_3)
            self.draw_text('Quit', self.font, (255, 255, 255), self.screen, 50, 405)

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            self.mainClock.tick(60)

    def ResumeGame(self):
        return

    def BackToMenu(self):
        running = True
        while running:
            Menu()

            pygame.display.update()
            self.mainClock.tick(60)

    def quit(self):
        pygame.quit()
        sys.exit()