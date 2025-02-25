#Nom : DIALLO
#Prenom : Oumou Tabara
import pydoc
class Service:
    """
        Classe de base pour les services disponibles dans le système de gestion du parking.

        Attributs:
            dateDemander (str): Date à laquelle le service est demandé.
            dateService (str): Date prévue pour l'exécution du service.
            rapport (str): Rapport lié à la réalisation du service.
        """
    def __init__(self, dateDemander, dateService, rapport):
        pass

class Maintenance(Service):
    """
        Service de maintenance pour les véhicules dans le parking.

        Inherits:
            Service: Classe de base pour les services.

        Methodes:
            effectuerMaintenance(): Exécute les opérations de maintenance sur le véhicule.
        """
    def __init__(self, dateDemander, dateService, rapport):
        pass
    def effectuerMaintenance(self):
        """Effectue la maintenance du véhicule."""
        pass

class Entretien(Service):
    """
        Service d'entretien pour les véhicules dans le parking.

        Inherits:
            Service: Classe de base pour les services.

        Methodes:
            effectuerEntretien(): Réalise l'entretien nécessaire sur le véhicule.
        """
    def __init__(self, dateDemander, dateService, rapport):
        pass
    def effectuerEntretien(self):
        """Effectue l'entretien du véhicule."""
        pass

class Livraison(Service):
    """
        Service de livraison de véhicules pour les clients du parking.

        Inherits:
            Service: Classe de base pour les services.

        Methodes:
            effectuerLivraison(): Effectue la livraison du véhicule au client.
        """
    def __init__(self, dateDemander, dateService, rapport):
        pass
    def effectuerLivraison(self):
        """Effectue la livraison du véhicule au client."""
        pass
pydoc.writedoc('Service')