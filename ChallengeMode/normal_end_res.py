import pygame.image

from ChallengeMode import image


class ner:
    def __init__(self, surface):
        self.surface = surface
        self.zero_star_img = image.load("NormalAssets/game_res/zero_star.png")
        self.one_star_img = image.load("NormalAssets/game_res/one_star.png")
        self.two_star_img = image.load("NormalAssets/game_res/two_star.png")
        self.three_star_img = image.load("NormalAssets/game_res/three_star.png")
        self.show_img = self.zero_star_img
        self.show_img_rect = self.show_img.get_rect(topleft=(0, 0))

