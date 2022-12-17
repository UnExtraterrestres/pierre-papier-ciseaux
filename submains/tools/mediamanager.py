# importation
import pygame

"""
type : ImageManager
comprend le chargement des images
"""


class ImageManager:

    # CONSTRUCTEUR
    def __init__(self):
        # PARAMETRES
        self.images = {
            "pierre": pygame.image.load(f"assets/entities/pierre.jpg"),
            "papier": pygame.image.load(f"assets/entities/papier.jpg"),
            "ciseaux": pygame.image.load(f"assets/entities/ciseaux.jpg")
        }
        for name in self.images:
            self.images[name] = pygame.transform.scale(self.images.get(name), (50, 50))


"""
type : SoundManager
comprend le chargement des fichiers audios
    une methode pour les jouer,
    une methode pour les arreter
"""


class SoundManager:

    # CONSTRUCTEUR
    def __init__(self):

        # PARAMETRES
        self.sounds = {
            "click": pygame.mixer.Sound("assets/sounds/click.ogg"),
            "pierre": pygame.mixer.Sound("assets/sounds/pierre.ogg"),
            "papier": pygame.mixer.Sound("assets/sounds/papier.ogg"),
            "ciseaux": pygame.mixer.Sound("assets/sounds/ciseaux.ogg")
        }

    # entree : music_name
    def play(self, music_name: str):
        self.sounds[music_name].play()

    # entree : music_name
    def stop(self, music_name: str):
        self.sounds[music_name].stop()


"""
________
|______|
|*(  )*|
|0|  |0|
"""
