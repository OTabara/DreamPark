#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi

import pydoc
from datetime import datetime, timedelta

from Placement import Placement


class Teleporteur:
    """Cette classe représente un système de téléportation pour des voitures
"""
    def __init__(self):
      """Initialise une nouvelle instance de la classe Teleporteur."""

    def teleporterVoiture(self, v, place):
        """cette methode permer de Téléporter une voiture ."""
        placement = Placement(dateDebut=datetime.today(), dateFin=datetime.today() + timedelta(days=1)) #Suppose que le placement fini le lendemain
        place.addPlacementP(placement)
        v.addPlacementV(placement)
        return placement

    def teleporterVoitureSuperAbonne(self, v, parking):
        """Téléporte une voiture d'un super abonné."""
        place = parking.trouverPlaceSuperAbonne(v)
        if place!= None :
            placement = Placement(dateDebut=datetime.today(), dateFin=datetime.today() + timedelta(days=1))
            place.addPlacementP(placement)
            v.addPlacementV(placement)
            return placement
        else :
            parking.parkingSuperAbonnes.append(v)
            print(f"Aucune place disponible, voiture {v.getImmatriculation()} ajoutée à la liste de parking spéciale.")
            return None


pydoc.writedoc('Teleporteur')