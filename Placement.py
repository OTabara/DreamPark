#Auteurs :Youssouf ali rozi et Oumou Tabara Diallo
import pydoc
class Placement :
    """
        Classe représentant un placement de voiture dans le parking.

        Attributs:
            dateDebut (date): Date de début du placement.
            dateFin (date): Date de fin du placement.
            estEncours (bool): Indique si le placement est en cours.

        Methodes:
            partirPlace(): Libère la place occupée par la voiture.
        """
    def __init__(self, dateDebut, dateFin):
        self.dateDebut = dateDebut
        self.dateFin = dateFin
        self.estEncours = False

    def getEstEncours(self):
        return self.estEncours

    def partirPlace(self):
        """Libère la place de stationnement pour la rendre disponible."""
        pass
    def __str__(self):
        return f"Placement du {self.dateDebut} au {self.dateFin}"

pydoc.writedoc('Placement')