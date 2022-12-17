# importation
from .tools.testeur import *

from random import randint
from math import cos, sin

import pygame.sprite

"""
type : Signe qui herite de Sprite
comprend l'image du signe, son nom, ces coordonnees
        et une fonction de deplacement
"""


class Signe(pygame.sprite.Sprite):

    def __init__(self, game, group, name: str, radius: int = 10, velocity: int = 10):
        super().__init__()
        # chargement des arguments
        self.game = game
        self.group = group
        self.name = name

        # PARAMETRES
        # image
        self.image = self.game.img.images.get(self.name)
        self.rect = self.image.get_rect()
        # position
        self.rect.x = randint(self.rect.width, self.game.screen.get_width()-self.rect.width)
        self.rect.y = randint(self.rect.height, self.game.screen.get_height()-self.rect.height)
        self.radius = radius
        self.velocity = [velocity, randint(0, 359)]

    def move(self):
        # incremente aleatoirement la position du signe

        # calcul du resultat (non stocke)
        # affectation des coordonnees
        if est_dans(self.rect.x + int(self.velocity[0]*cos(self.velocity[1])), self.game.screen.get_width()):
            self.rect.x += int(self.velocity[0]*cos(self.velocity[1]))
        if est_dans(self.rect.y + int(self.velocity[0]*sin(self.velocity[1])), self.game.screen.get_height()):
            self.rect.y += int(self.velocity[0]*sin(self.velocity[1]))

        # affectation de la vitesse
        self.velocity[1] += randint(-2, 2)

        # verification des collisions
        self.set_signe()

    def set_signe(self):
        # change le signe en fonction des regles du jeu

        for signe in [self.game.current_scene.pierres,
                      self.game.current_scene.papiers,
                      self.game.current_scene.ciseaux]:
            for entity in pygame.sprite.spritecollide(self, signe, False):
                if self.name != entity.name:
                    if is_better_than(self, entity):
                        # changement de l'entitee
                        entity.set_group(self)
                    else:
                        # changement de self
                        self.set_group(entity)

    # entree : entity
    def set_group(self, entity):
        # passe self dans le groupe de entity

        # calcul du resultat (non stocke)
        # joue le son de l'entity
        self.game.sounds.play(entity.name)
        # changer le nom
        self.name = entity.name
        # changer l'image
        self.image = self.game.img.images.get(self.name)
        # changer le groupe
        self.group.remove(self)
        self.group = entity.group
        self.group.add(self)


"""
________
|______|
|*(  )*|
|0|  |0|
"""
