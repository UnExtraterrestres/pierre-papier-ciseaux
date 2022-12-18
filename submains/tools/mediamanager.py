# importation
import pygame

import os


# entree : root
def load_files_in(root: str):
    # renvois un dictionnaire avec les fichiers charges

    # declaration du resultat
    loaded_files = {}

    # calcul du resultat
    for path, sub_dirs, files in os.walk(root):
        for name in files:
            if "images" in root:
                loaded_files[name[0:-4]] = pygame.image.load(os.path.join(path, name))
            elif "sounds" in root:
                loaded_files[name[0:-4]] = pygame.mixer.Sound(os.path.join(path, name))

    # renvois du resultat
    return loaded_files


"""
type : ImageManager
comprend le chargement des images
"""


class ImageManager:

    # CONSTRUCTEUR
    def __init__(self):
        # PARAMETRES
        self.images = load_files_in("assets/images")
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
        self.sounds = load_files_in("assets/sounds")

    #  : music_name
    def play(self, music_name: str):
        self.sounds[music_name].play()

    #  : music_name
    def stop(self, music_name: str):
        self.sounds[music_name].stop()


"""
________
|______|
|*(  )*|
|0|  |0|
"""
