# importations
import pygame.display

from .scene import *


"""
type : Simulateur
comprend la gestion de l'ecran (screen),
    une methode pour la boucle du jeu,
    un etat de la simulation,
    une methode pour afficher du texte sur l'ecran
"""


class Simulateur:

    # CONSTRUCTEUR
    def __init__(self, default_fps: int, size: tuple, title: str):

        # PARAMETRES
        # etat du jeu
        self.is_running = True
        # FPS
        self.clock = pygame.time.Clock()
        self.current_fps = default_fps
        # police
        self.font = pygame.font.SysFont("monospace", 16)
        # scene courrante
        self.current_scene = Scene(self)
        # gestionnaires d'images et de sons
        self.img = ImageManager()
        self.sounds = SoundManager()
        # ecran
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        pygame.display.set_icon(self.img.images.get("papier"))

    def run(self):
        # lance la boucle de jeu

        # calcul du resultat
        while self.is_running:
            # interactions utilisateur-jeu
            self.current_scene.check_event()
            # logique de la scene
            self.current_scene.update()
            # affichages de la scene
            self.current_scene.display()
            # tick des FPS
            self.clock.tick(self.current_fps)

    # entree : text
    # entree : coord
    # entree : color
    def pin_up(self, text: str, coord: tuple, color=(0, 0, 0)):
        # affiche text en color a la position coord de l'ecran

        # declaration de la donnee
        txt = self.font.render(text, True, color)

        # calcul du resultat
        self.screen.blit(txt, coord)


"""
________
|______|
|*(  )*|
|0|  |0|
"""
