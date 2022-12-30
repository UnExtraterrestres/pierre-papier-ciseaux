from random import randint

"""
Type : Settings
comprend des parametres pour rendre dynamique le contenu de la simulation,
    afficher les détails,
    nombre de pierres,
    nombre de papiers,
    nombre de ciseaux
"""


class Settings:

    # CONSTRUCTEUR
    def __init__(self, simu):
        # chargement de l'argument
        self.simu = simu

        # PARAMETRES
        # affichage des détails
        self.display_details = True
        # nombre de pierres, de papiers et de ciseaux
        self.num_rock = randint(1, 20)
        self.num_paper = randint(1, 20)
        self.num_scissor = randint(1, 20)


"""
________
|______|
|*(  )*|
|0|  |0|
"""
