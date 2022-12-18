# importation
from submains.simulateur import *

if __name__ == '__main__':
    # ouverture et fermeture du simulateur

    # declaration de la donnee
    # initialisation de pygame
    pygame.init()
    simulateur = Simulateur(12, (800, 600), "Simulateur - PPC")
    # calcul du resultat
    # ouverture du simulateur
    simulateur.current_scene.set_current_scene(Menu(simulateur))
    # fermeture
    pygame.quit()


"""
________
|______|
|*(  )*|
|0|  |0|
"""
