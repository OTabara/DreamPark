#Auteurs :Youssouf ali rozi et Oumou Tabara Diallo
from datetime import datetime, timedelta

import pydoc

from Abonnement import Abonnement
from Contrat import Contrat
from Voiture import Voiture


class Client:
    """
        Classe représentant un client dans le système de gestion de parking.

        Attributs:
            nom (str): Nom du client.
            adresse (str): Adresse du client.
            estAbonné (bool): Indique si le client est abonné.
            estSuperAbonné (bool): Indique si le client est super-abonné.

        Methodes:
            sAbonner(): Abonne le client au service de parking.
            nouvelleVoiture(): Ajoute une nouvelle voiture au compte du client.
            seDesabonner(): Désabonne le client.
            demanderMaintenance(): Demande un service de maintenance pour le véhicule.
            demanderLivraison(): Demande une livraison de voiture.
            demandeEntretien(): Demande un service d'entretien.
            entrerParking(): Enregistre l'entrée du client dans le parking.
    """
    def __init__(self, nom, adresse, voiture):
        self.nom = nom
        self.adresse = adresse
        self.estAbonne = False
        self.estSuperAbonne = False
        self.Voiture = voiture

    def getVoiture(self):
        return self.Voiture
    def getNom(self):
        return self.nom

    def getEstAbonne(self):
        return self.estAbonne

    def getEstSuperAbonne(self):
        return self.estSuperAbonne

    def sAbonner(self, abonnement):
        """Abonne le client au service de parking."""
        # Obtenir la date actuelle
        date_debut = datetime.now().strftime("%d-%m-%Y")  # Format jj-mm-aa

        # Calculer la date de fin (un an après la date actuelle)
        date_fin = (datetime.now() + timedelta(days=365)).strftime("%d-%m-%Y")  # Format jj-mm-aa

        # Créer un contrat avec les dates calculées
        contrat = Contrat(date_debut, date_fin)
        abonnement.addContrat(contrat)
        if abonnement.estPackGarantie:
            self.estSuperAbonne = True
        else : self.estAbonne = True

    def nouvelleVoiture(self, imma, hauteurV, longueurV):
        """Ajoute une nouvelle voiture pour le client."""
        self.Voiture = Voiture(imma, hauteurV, longueurV)

    def seDesabonner(self):
        """Désabonne le client."""
        if self.estAbonne:
            self.estAbonne = False
        else:
            self.estSuperAbonne = False

    def demanderMaintenance(self):
        """Demande un service de maintenance pour la voiture du client."""
        pass
    def demanderLivraison(self ):
        """Demande la livraison de la voiture du client."""
        pass
    def demanderEntretien(self):
        """Demande un service d'entretien pour la voiture du client."""
        pass
    def entrerParking(self):
        """Enregistre l'entrée du client dans le parking."""
        pass

pydoc.writedoc('Client')