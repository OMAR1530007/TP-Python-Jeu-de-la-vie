import random

def creer_grille(n, m):
    grille = []
    for _ in range(n):
        ligne = [random.randint(0, 1) for _ in range(m)]
        grille.append(ligne)
    return grille


n = 60
m = 10
grille = creer_grille(n, m)
for ligne in grille:
    print(ligne)