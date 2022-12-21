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


personnage = Caracteristiques(random.randint(1, 20), random.randint(1, 20), random.randint(1, 20),
                              random.randint(1, 20), random.randint(1, 20), random.randint(1, 20))

# afficher les caractéristiques du personnage
print(f"Force           : {personnage.force}")
print(f"Dexterite       : {personnage.dexterite}")
print(f"Constitution    : {personnage.constitution}")
print(f"Intelligence    : {personnage.intelligence}")
print(f"Sagesse         : {personnage.sagesse}")
print(f"Charisme        : {personnage.charisme}")
