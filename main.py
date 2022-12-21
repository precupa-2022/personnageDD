"""
Programme fait par Alexander Precup
Groupe: 402
Description: Objets orientées
Exercise 5 - Écrire une dataclass pour les caractéristiques d'un personnage D&D
"""
from dataclasses import dataclass
import random


@dataclass
class Caracteristiques:
    force: int
    dexterite: int
    constitution: int
    intelligence: int
    sagesse: int
    charisme: int


class Stats:
    def __init__(self):
        self.personnage = Caracteristiques(random.randint(1, 20), random.randint(1, 20), random.randint(1, 20),
                                           random.randint(1, 20), random.randint(1, 20), random.randint(1, 20))


stats = Stats()

# afficher les caractéristiques du personnage
print(f"Force           : {stats.personnage.force}")
print(f"Dexterite       : {stats.personnage.dexterite}")
print(f"Constitution    : {stats.personnage.constitution}")
print(f"Intelligence    : {stats.personnage.intelligence}")
print(f"Sagesse         : {stats.personnage.sagesse}")
print(f"Charisme        : {stats.personnage.charisme}")
