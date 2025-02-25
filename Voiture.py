#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi
import pydoc
class Voiture :
    """
        Classe représentant un véhicule dans le système de parking.

        Attributs:
            hauteur (float): Hauteur de la voiture.
            longueur (float): Longueur de la voiture.
            immatriculation (str): Numéro d'immatriculation de la voiture.
            estDansParking (bool): Statut indiquant si la voiture est dans le parking.

        Methodes:
            addPlacementV(): Ajoute un placement pour la voiture.
        """
    def __init__(self, hauteur, longueur, immatriculation):
        self.hauteur = hauteur
        self.longueur = longueur
        self.immatriculation = immatriculation
        self.estDansParking = False
        self.PlacementV = None

    def getHauteur(self):
        return self.hauteur

    def getLongueur(self):
        return self.longueur

    def getImmatriculation(self):
        return self.immatriculation

    def getEstDansParking(self):
        return self.estDansParking

    def setEstDansParking(self, estDansParking):
        self.estDansParking = estDansParking

    def getPlacementV(self):
        return self.PlacementV

    def addPlacementV(self, placement):
        """Ajoute un placement pour la voiture."""
        self.PlacementV = placement
        placement.estEncours = True
        print(f"Placement ajouté pour la voiture {self.immatriculation}.")


pydoc.writedoc('Voiture')