#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi
import pydoc

class Abonnement:
    """Cette classe représente un abonnement pour le service de parking."""
    def __init__(self,libelle,prix) :
        """
         libelle  : Description de l'abonnement.
         prix:le Coût de l'abonnement.
        estPackGar: Indique si l'abonnement fait partie d'un pack garanti.
        """
        self.libelle = libelle
        self.prix = prix
        self.estPackGarantie = False
        self.contrat = None



    def getEstPackGar(self):
        return self.estPackGarantie

    def setEstPackGar(self,estPackGar):
        self.estPackGarantie = estPackGar

    def getContrat(self):
        return self.contrat

    def addContrat(self, contrat):
        """Ajoute un contrat associé à un abonnement"""
        self.contrat = contrat

pydoc.writedoc('Abonnement')