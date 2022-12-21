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
    """
     Classe Caracteristiques
        dataclass attributs de type statistique force, dexterite, constitution, intelligence, sagesse, charisme
        avec des valeurs initiales un numéro aléatoire de 1 a 20
    """
    force: int = random.randint(1, 20)
    dexterite: int = random.randint(1, 20)
    constitution: int = random.randint(1, 20)
    intelligence: int = random.randint(1, 20)
    sagesse: int = random.randint(1, 20)
    charisme: int = random.randint(1, 20)


class Stats:
    def __init__(self):
        self.personnage = Caracteristiques()


stats = Stats()

# afficher les caractéristiques du personnage
print(f"Force           : {stats.personnage.force}")
print(f"Dexterite       : {stats.personnage.dexterite}")
print(f"Constitution    : {stats.personnage.constitution}")
print(f"Intelligence    : {stats.personnage.intelligence}")
print(f"Sagesse         : {stats.personnage.sagesse}")
print(f"Charisme        : {stats.personnage.charisme}")
