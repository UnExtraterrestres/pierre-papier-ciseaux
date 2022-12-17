# importation
from .tools.mediamanager import *

from .signes import *

"""
type : Scene
comprend une description des etapes de la boucle de jeu
     et une methode pour modifier la scene courrante du simulateur
"""


class Scene:

    # CONSTRUCTEUR
    def __init__(self, game):
        # chargement de l'argument
        self.game = game

        # PARAMETRES
        self.pressed = {}

    def check_event(self):
        # verifie les entrees utilisateur
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                # check the closing
                self.game.is_running = False
            # get key pressed
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
            # get key release
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False

        # lorsque <w> est appuye on arrete la simulation
        if self.pressed.get(pygame.K_w):
            # joue le son
            self.game.sounds.play("click")

            # affectation de l'etat du simulateur la simulation
            self.game.is_running = False

    def update(self):
        # applique la logique de la scene
        pass

    def display(self):
        # affiche la scene

        # affichage du fond
        self.game.screen.fill((200, 200, 200))

        # NB : penser pour chaque scene a flip pygame apres les affichages

    # entree : scene
    def set_current_scene(self, scene):
        # affecte scene comme nouvelle scene courrante
        # puis lance la boucle de jeu

        # affecte la scene courrante
        self.game.current_scene = scene

        # appel la boucle de jeu
        self.game.run()


"""
type : Menu qui herite de Scene
comprend une description du menu du simulateur
"""


class Menu(Scene):

    # CONSTRUCTEUR
    def __init__(self, game):
        # chargement de l'argument
        super().__init__(game)

    def check_event(self):
        # lorsque <return> est appuye : joue un son et passe au corps

        # calcul de la donnee
        super().check_event()

        if self.pressed.get(pygame.K_RETURN):
            # joue le son
            self.game.sounds.play("click")

            # change la scene courrante
            self.set_current_scene(Corps(self.game))

    def update(self):
        super().update()

    def display(self):
        super().display()

        # affichage du texte
        self.game.pin_up("appuyer sur <entrer> pour commencer",
                         (10, 10))
        self.game.pin_up("appuyer sur <w> pour arreter la simulation",
                         (10, 30))

        # flip pygame
        pygame.display.flip()


"""
type : Corps qui herite de Scene
comprend une description du corps du simulateur
"""


class Corps(Scene):

    # CONSTRUCTEUR
    def __init__(self, game):
        # chargement de l'argument
        super().__init__(game)

        # PARAMETRES
        # pierres
        self.pierres = pygame.sprite.Group()
        # papiers
        self.papiers = pygame.sprite.Group()
        # ciseaux
        self.ciseaux = pygame.sprite.Group()

        # affectation des parametres
        # signes
        for i in range(randint(10, 20)):
            self.pierres.add(Signe.__call__(self.game, self.pierres, "pierre"))
            self.papiers.add(Signe.__call__(self.game, self.papiers, "papier"))
            self.ciseaux.add(Signe.__call__(self.game, self.ciseaux, "ciseaux"))

    def check_event(self):
        super().check_event()

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
                self.game.screen.blit(entity.image, entity.rect)

        # affichages des stats
        self.game.pin_up(f"Nombre de pierres : {len(self.pierres)}", (10, 10))
        self.game.pin_up(f"Nombre de papiers : {len(self.papiers)}", (10, 30))
        self.game.pin_up(f"Nombre de ciseaux : {len(self.ciseaux)}", (10, 50))

        # flip pygame
        pygame.display.flip()


"""
________
|______|
|*(  )*|
|0|  |0|
"""
