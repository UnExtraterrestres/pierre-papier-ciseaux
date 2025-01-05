# importation
import tkinter

from .tools.mediamanager import *
from .tools.application.application import *

from .signes import *

"""
type : Scene
comprend une description des etapes de la boucle de jeu
     et une methode pour modifier la scene courrante du simulateur
"""


class Scene:

    # CONSTRUCTEUR
    def __init__(self, simu):
        # chargement de l'argument
        self.simu = simu

        # PARAMETRES
        self.pressed = {}

    def check_event(self):
        # verifie les entrees utilisateur
        # w : arrête le programme à tout moment

        # calcul du resultat
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                # check the closing
                self.simu.is_running = False
            # get key pressed
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
            # get key release
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False

        # lorsque <w> est appuye on arrête la simulation
        if self.pressed.get(pygame.K_w):
            # joue le son
            self.simu.sounds.play("click")

            # affectation de l'etat du simulateur la simulation
            self.simu.is_running = False

    def update(self):
        # applique la logique de la scene
        pass

    def display(self):
        # affiche la scene

        # affichage du fond
        self.simu.screen.fill((200, 200, 200))

        # NB : penser pour chaque scene a flip pygame apres les affichages

    # entree : scene
    def set_current_scene(self, scene):
        # affecte scene comme nouvelle scene courrante
        # puis lance la boucle de jeu

        # affecte la scene courrante
        self.simu.current_scene = scene

        # appel la boucle de jeu
        self.simu.run()


"""
type : Menu qui herite de Scene
comprend une description du menu du simulateur
"""


class Menu(Scene):

    # CONSTRUCTEUR
    def __init__(self, simu):
        # chargement de l'argument
        super().__init__(simu)

        # PARAMETRES
        # curseur
        self.cursor = 50
        # application
        self.app = App(self.simu)

    def check_event(self):
        # verifie les entrées utilisateur
        # <return> est appuye : lance le corps de la simulation
        # les fleches haut et bas, font respectivement monter et descendre le curseur

        # calcul de la donnee
        super().check_event()

        # touche : entrer
        if self.pressed.get(pygame.K_RETURN):
            # commencer
            if self.cursor == 50:
                # joue le son
                self.simu.sounds.play("click")

                # change la scene courrante
                self.set_current_scene(Corps(self.simu))
            # touches
            elif self.cursor == 70:
                # joue le son
                self.simu.sounds.play("click")

                # ouvre la fenêtre des touches
                try:
                    self.app.keys.display_widgets()
                    self.app.mainloop()
                except _tkinter.TclError:
                    self.app = App(self.simu)
                    self.app.keys.display_widgets()
                    self.app.mainloop()
            # parametres
            elif self.cursor == 90:
                # joue le son
                self.simu.sounds.play("click")

                # ouvre la fenêtre des parametres
                try:
                    self.app.settings.display_widgets()
                    self.app.mainloop()
                except _tkinter.TclError:
                    self.app = App(self.simu)
                    self.app.settings.display_widgets()
                    self.app.mainloop()
            # quitter
            elif self.cursor == 110:
                # joue le son
                self.simu.sounds.play("click")

                # arrête la simulation
                # affectation de l'etat du simulateur la simulation
                self.simu.is_running = False

            del self.pressed[pygame.K_RETURN]

        # touche : fleche du haut
        if self.pressed.get(pygame.K_UP):
            # test le curseur
            if self.cursor - 20 >= 50:
                # joue le son
                self.simu.sounds.play("click")
                # fait monter le curseur
                self.cursor -= 20
            del self.pressed[pygame.K_UP]

        # touche : fleche du bas
        elif self.pressed.get(pygame.K_DOWN):
            # test le curseur
            if self.cursor + 20 <= 110:
                # joue le son
                self.simu.sounds.play("click")
                # fait descendre le curseur
                self.cursor += 20
            del self.pressed[pygame.K_DOWN]

    def update(self):
        super().update()

    def display(self):
        super().display()

        # affichage du texte
        self.simu.pin_up("Commencer",
                         (int(self.simu.screen.get_width()/2), 50))
        self.simu.pin_up("Touches",
                         (int(self.simu.screen.get_width()/2), 70))
        self.simu.pin_up("Parametres",
                         (int(self.simu.screen.get_width()/2), 90))
        self.simu.pin_up("Quitter",
                         (int(self.simu.screen.get_width() / 2), 110))

        # affichage du curseur
        pygame.draw.rect(self.simu.screen, (100, 100, 100),
                         (int(self.simu.screen.get_width()/2)-26, self.cursor,
                          7, 16))

        # flip pygame
        pygame.display.flip()


"""
type : Corps qui herite de Scene
comprend une description du corps du simulateur
"""


class Corps(Scene):

    # CONSTRUCTEUR
    def __init__(self, simu):
        # chargement de l'argument
        super().__init__(simu)

        # PARAMETRES
        # pierres
        self.pierres = pygame.sprite.Group()
        # papiers
        self.papiers = pygame.sprite.Group()
        # ciseaux
        self.ciseaux = pygame.sprite.Group()

        # affectation des parametres
        # signes
        for _ in range(self.simu.settings.num_rock):
            self.pierres.add(Signe.__call__(self.simu, self.pierres, "pierre"))
        for _ in range(self.simu.settings.num_paper):
            self.papiers.add(Signe.__call__(self.simu, self.papiers, "papier"))
        for _ in range(self.simu.settings.num_scissor):
            self.ciseaux.add(Signe.__call__(self.simu, self.ciseaux, "ciseaux"))

    def check_event(self):
        # verifie les entrées utilisateur
        # m : ouvre le menu principal

        # calcul du resultat
        super().check_event()

        if self.pressed.get(pygame.K_m):
            # joue le son
            self.simu.sounds.play("click")

            # affectation de la scene courrante
            self.set_current_scene(Menu(self.simu))

            del self.pressed[pygame.K_m]

    def update(self):
        super().update()

        # deplacement des signes
        for signe in [self.pierres, self.papiers, self.ciseaux]:
            for entity in signe:
                entity.move()

    def display(self):
        super().display()

        # affichage des signes
        for signe in [self.pierres, self.papiers, self.ciseaux]:
            for entity in signe:
                self.simu.screen.blit(entity.image, entity.rect)

        # affichages des stats
        if self.simu.settings.display_details:
            self.simu.pin_up(f"Nombre de pierres : {len(self.pierres)}", (10, 10))
            self.simu.pin_up(f"Nombre de papiers : {len(self.papiers)}", (10, 30))
            self.simu.pin_up(f"Nombre de ciseaux : {len(self.ciseaux)}", (10, 50))

        # flip pygame
        pygame.display.flip()


"""
________
|______|
|*(  )*|
|0|  |0|
"""
