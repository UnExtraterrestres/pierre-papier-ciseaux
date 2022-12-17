# entree : entity_0
# entree : entity_1
def is_better_than(entity_0, entity_1):
    # renvois : vrai si entity_0 est meilleure que entity_1 d'apres les regles du jeu

    # declaration du resultat
    is_better = True

    # calcul du resultat
    if entity_0.name == "pierre" and entity_1.name == "papier":
        is_better = False
    elif entity_0.name == "papier" and entity_1.name == "ciseaux":
        is_better = False
    elif entity_0.name == "ciseaux" and entity_1.name == "pierre":
        is_better = False

    # renvois du resultat
    return is_better


# entree : nombre
# entree : borne_sup
# entree : borne_inf
def est_dans(nombre, borne_sup, borne_inf=0):
    # renvois : vrai si nombre est compris entre borne_inf et borne_sup

    # verification des arguments
    if borne_inf > borne_sup:
        # permutation des bornes
        borne_inf, borne_sup = borne_sup, borne_inf

    # renvois du resultat (non stocke)
    return borne_inf <= nombre <= borne_sup


"""
________
|______|
|*(  )*|
|0|  |0|
"""
