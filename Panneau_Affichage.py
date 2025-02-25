#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi

import pydoc


class Panneau_Affichage:
    """Cette classe représente un panneau d'affichage qui affiche
       des informations, qui est le nombre de places disponibles."""

    def __init__(self):
        """Initialise une instance de la classe Panneau_Affichage."""

    def afficherNbPlacesDisponibles(self, parking):
        """Affiche le nombre de places disponibles."""

        return f"Le nombre de places disponibles est : {parking.getPlacesLibres()}"


pydoc.writedoc('Panneau_Affichage')