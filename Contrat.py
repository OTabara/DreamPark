#Auteurs :Youssouf ali rozi et Oumou Tabara Diallo
import pydoc
class Contrat:
    """Cette classe représente un contrat avec une date de début,
    une date de fin et un état indiquant s'il est en cours ou non"""
    def __init__(self, dateDebut, dateFin):
        """Initialise une nouvelle instance de la classe Contrat."""
        self.dateDebut = dateDebut
        self.dateFin = dateFin
        self.estEncours = True

    def getEstEncours(self):
        return self.estEncours

    def rompreContrat(self):
        """cette methode rompt le contrat en cours."""
        self.estEncours = False

pydoc.writedoc('Contrat')