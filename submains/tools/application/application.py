# importation
from .widgets import *

"""
type : App
comprend des widgets,
    permet leur regroupement, leur gestion...
"""


class App(Tk):

    # CONSTRUCTEUR
    def __init__(self, simu):
        # chargement de l'argument
        self.simu = simu

        # PARAMETRES
        # superclass
        super().__init__()
        # configuration de la fenetre
        self.title("PPC - Interface")
        self.geometry("400x500")
        self.resizable(width=None, height=None)
        # widgets des fenêtres
        # touches
        self.keys = WinKeys(self)
        # parametres
        self.settings = WinSettings(self)


"""
________
|______|
|*(  )*|
|0|  |0|
"""
