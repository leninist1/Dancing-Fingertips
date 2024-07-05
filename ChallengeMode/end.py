import pygame
import sys

from PIL.ImageQt import rgb

from ChallengeMode import image


def restart_game(game):
    game.reset()


def show_victory_screen(screen, game, score):
    background = image.load("NormalAssets/game_res/one_star.png", size=(1200, 700))
    # -----------------------------------------------------------
    if 60 <= score <= 80:
        background = image.load("NormalAssets/game_res/two_star.png", size=(1200, 700))
    elif score > 80:
        background = image.load("NormalAssets/game_res/three_star.png", size=(1200, 700))
    # -----------------------------------------------------------
    screen.blit(background, (0, 0))
    wait_for_restart(screen, game)


def show_defeat_screen(screen, game, score):
    background = image.load("NormalAssets/game_res/zero_star.png", size=(1200, 700))
    screen.blit(background, (0, 0))
    wait_for_restart(screen, game)


def draw_button(screen, text, position, action=None):
    font = pygame.font.SysFont(None, 55)
    text_render = font.render(text, True, (255, 255, 255))
    text_rect = text_render.get_rect(center=position)
    button_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10, text_rect.width + 20, text_rect.height + 20)
    pygame.draw.rect(screen, (0, 0, 0), button_rect)  # Draw button
    screen.blit(text_render, text_rect)
    return button_rect


def wait_for_restart(screen, game):
    # restart_button = draw_button(screen, 'Continue', (screen.get_width() / 2, screen.get_height() / 2 + 100))
    # pygame.display.flip()
    rect1 = image.load("NormalAssets/game_res/restart.png",size=(100, 100)).get_rect(topleft=(365, 390))
    rect2 = image.load("NormalAssets/game_res/home.png",size=(100, 100)).get_rect(topleft=(550, 390))
    rect3 = image.load("NormalAssets/game_res/sound.png",size=(100, 100)).get_rect(topleft=(730, 390))
    # rect1 = pygame.draw.rect(screen, color=rgb(255, 255, 255, 0),  rect=(365, 390, 100, 100))
    # rect2 = pygame.draw.rect(screen, color=rgb(255, 255, 255, 0), rect=(550, 390, 100, 100))
    # rect3 = pygame.draw.rect(screen, color=rgb(255, 255, 255, 0), rect=(730, 390, 100, 100))
    pygame.display.flip()
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint(pygame.mouse.get_pos()):
                    # pygame.quit()
                    # sys.exit()
                    restart_game(game)  # Assuming restart_game is properly defined to reset the game
                    flag = False
                elif rect2.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                elif rect3.collidepoint(pygame.mouse.get_pos()):
                    print(3)
            """ if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                flag = False """
