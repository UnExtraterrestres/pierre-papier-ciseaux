# importation
from tkinter import *

from random import randint

"""
comprennent une application,
    on décrit l'ensemble des widgets d'une fenêtre
"""


class WinKeys:

    # CONSTRUCTEUR
    def __init__(self, app):
        # chargement de l'argument
        self.app = app

        # PARAMETRES
        # widgets
        self.widgets = [
            Label(self.app, text="Quitter la simulation : w"),
            Label(self.app, text="Ouvrir le menu principal : m")
        ]

    def display_widgets(self):
        # affiche les widgets

        # affichage du resultat
        # affectation du titre de l'application
        self.app.title("PPC - Touches")
        # affichage des widgets
        for index, widget in enumerate(self.widgets):
            widget.grid(column=0, row=index)


class WinSettings:

    # CONSTRUCTEUR
    def __init__(self, app):
        # chargement de l'argument
        self.app = app

        # PARAMETRES
        # detection de touche
        self.app.bind("<Button-1>", lambda arg: self.display_widgets())
        # afficher les détails
        self.details = BooleanVar()
        self.details.set(True)
        # affecter aléatoirement le nombre de signes
        self.randomly = BooleanVar()
        self.randomly.set(True)
        # widgets
        self.widgets = [
            Label(self.app, text="- Afficher les détails"),
            Radiobutton(self.app, variable=self.details, text="Oui", value=True),
            Radiobutton(self.app, variable=self.details, text="Non", value=False),
            Label(self.app, text="- Nombre de signes"),
            Radiobutton(self.app, variable=self.randomly, text="Manuel", value=False),
            Radiobutton(self.app, variable=self.randomly, text="Aléatoire", value=True),
            Scale(self.app, label="Pierre", orient="horizontal",
                  from_=1, to=50, resolution=1, tickinterval=5, length=300),
            Scale(self.app, label="Papier", orient="horizontal",
                  from_=1, to=50, resolution=1, tickinterval=5, length=300),
            Scale(self.app, label="Ciseaux", orient="horizontal",
                  from_=1, to=50, resolution=1, tickinterval=5, length=300),
            Button(self.app, text="Appliquer", command=self.to_apply)
        ]

    def display_widgets(self):
        # affiche les widgets

        # affichage du resultat
        # affectation du titre de l'application
        self.app.title("PPC - Parametres")
        # affichage des widgets
        # Afficher les détails
        self.widgets[0].grid(column=0, row=0)
        self.widgets[1].grid(column=0, row=1)
        self.widgets[2].grid(column=1, row=1)
        # Nombre de signes
        self.widgets[3].grid(column=0, row=2)
        self.widgets[4].grid(column=0, row=3)
        self.widgets[5].grid(column=1, row=3)
        if not self.randomly.get():
            self.widgets[6].grid(column=0, row=4)
            self.widgets[7].grid(column=0, row=5)
            self.widgets[8].grid(column=0, row=6)

        # Appliquer les paramètres
        self.widgets[-1].place(x=300, y=460, width=100, height=40)

    def to_apply(self):
        # Change les parametres de la simulation
        # suivant les valeurs entrées

        # renvois du resultat
        # afficher les détails
        self.app.simu.settings.display_details = self.details.get()
        # définir le nombre de signes
        if self.randomly.get():
            # on affecte le nombre de signes aléatoirement
            self.app.simu.settings.num_rock = randint(1, 20)
            self.app.simu.settings.num_paper = randint(1, 20)
            self.app.simu.settings.num_scissor = randint(1, 20)
        else:
            # on prend les valeurs des curseurs
            self.app.simu.settings.num_rock = self.widgets[6].get()
            self.app.simu.settings.num_paper = self.widgets[7].get()
            self.app.simu.settings.num_scissor = self.widgets[8].get()

        # ferme la fenetre
        self.app.destroy()


"""
________
|______|
|*(  )*|
|0|  |0|
"""
