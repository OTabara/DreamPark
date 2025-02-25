#Auteurs :Youssouf ali rozi et Oumou Tabara Diallo
import unittest
import pydoc

from Abonnement import Abonnement
from Client import Client
from Voiture import Voiture
from main import voiture2


class TestClient(unittest.TestCase):
    """Tests des fonctionnalités de la classe Client."""
    def setUp(self):
        """Configuration du cas de test, initialisation des objets nécessaires."""
        self.voiture1 = Voiture(2.0, 4.0, "AB-123-CD")
        self.voiture2 = Voiture(1.8, 4.2, "XY-987-ZT")
        self.client1 = Client("Ali", "6 chemin edgard varese", self.voiture1)
        self.client2 = Client("Oumou", "34 Avenue de l'hers", self.voiture2)
        self.abonnement1= Abonnement("Annuelle", 300)
        self.abonnement2 = Abonnement("Annuelle", 300)
        self.abonnement2.setEstPackGar(True)
        self.client1.sAbonner(self.abonnement1)
        self.client2.sAbonner(self.abonnement2)


    def tearDown(self):
        """Nettoyage après le test."""
        self.voiture1 = self.voiture2 = None
        self.client1 = None
        self.client2 = None
    def test_client(self):
        """Test des fonctionnalités de base du client."""
        self.assertIsNotNone(self.client1,"Le client n'a pas été créé")

    def test_sAbonner(self):
        """Test de la fonctionnalité d'abonnement du client."""
        self.assertTrue(self.client1.getEstAbonne(),"Le client n'est pas un abonné")
        self.assertFalse(self.client1.getEstSuperAbonne(), "Le client n'est pas un Superabonné")
        self.assertTrue(self.client2.getEstSuperAbonne(), "Le client n'est pas un Superabonné")
        self.assertFalse(self.client2.getEstAbonne(), "Le client est pas un abonné")

    def test_seDesabonner(self):
        """Test de la fonctionnalité de désabonnement du client."""
        self.client1.seDesabonner()
        self.assertFalse(self.client1.getEstAbonne() and self.client1.getEstSuperAbonne())
        self.client2.seDesabonner()
        self.assertFalse(self.client2.getEstAbonne() and self.client2.getEstSuperAbonne())
    def test_nouvelleVoiture(self):
        """Test de l'ajout d'une nouvelle voiture au client."""
        pass
    def test_demanderMaintenance(self):
        """Test de la demande de service de maintenance par le client."""
        pass
    def test_demanderEntretien(self):
        """Test de la demande de service d'entretien par le client."""
        pass
    def test_demanderLivraison(self):
        """Test de la demande de service de livraison par le client."""
        pass
    def test_entrerParking(self):
        """Test de la capacité du client à entrer dans le parking."""
        pass
pydoc.writedoc('TestClient')