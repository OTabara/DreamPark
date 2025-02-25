#Auteurs :Youssouf ali rozi et Oumou Tabara Diallo

import pydoc
class Place :
    """
        Classe représentant une place de parking.

        Attributs:
            numero (int): Numéro unique de la place.
            niveau (char): Niveau où se trouve la place.
            longueur (float): Longueur de la place.
            estlibre (bool): Indique si la place est libre.
            hauteur (float): Hauteur de la place.

        Methodes:
            addPlacementP(): Ajoute un placement sur la place de parking.
        """
    def __init__(self, numero, niveau, longueur, hauteur) :
        self.numero = numero
        self.niveau = niveau
        self.longueur = longueur
        self.estlibre = True
        self.hauteur = hauteur
        self.placementP = None

    def getNumero(self):
        return self.numero

    def getNiveau(self):
        return self.niveau
    def getHauteur(self) :
        return self.hauteur

    def getLongueur(self) :
        return self.longueur

    def getEstLibre(self) :
        return self.estlibre

    def setEstLibre(self, estlibre):
        self.estlibre = estlibre

    def getPlacementP(self):
        return self.placementP

    def addPlacementP(self, placement):
        """Ajoute un placement sur la place de parking."""
        if self.estlibre:
            self.placementP = placement
            placement.estEncours = True
            self.estlibre = False
            print(f"la place {self.niveau}{self.numero} a bien été affectée ")
        else :
            print("la place est déjà occupée")
pydoc.writedoc('Place')