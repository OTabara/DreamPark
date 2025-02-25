#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi

import unittest
import pydoc


from Client import Client
from Service import Maintenance, Entretien, Livraison
from Voiturier import Voiturier
from Voiture import Voiture
from Place import Place
from Placement import Placement



class TestService(unittest.TestCase):
    """Tests des fonctionnalités de la classe Service."""
    def setUp(self):
        """Configuration du cas de test pour les services."""
        pass
    def tearDown(self):
        """Nettoyage après le test des services."""
        pass

class TestMaintenance(unittest.TestCase):
    """Tests des fonctionnalités du service de Maintenance."""
    def setUp(self):
        """Configuration du cas de test pour le service de maintenance."""
        pass
    def tearDown(self):
        """Nettoyage après le test de maintenance."""
        pass
    def test_effectuerMaintenance(self):
        """Test de l'exécution des services de maintenance."""
        pass

class TestEntretien(unittest.TestCase):
    """Tests des fonctionnalités du service d'Entretien."""
    def setUp(self):
        """Configuration du cas de test pour le service d'entretien."""
        pass
    def tearDown(self):
        """Nettoyage après le test d'entretien."""
        pass
    def test_effectuerEntretien(self):
        """Test de l'exécution des services d'entretien."""
        pass

class TestLivraison(unittest.TestCase):
    """Tests des fonctionnalités du service de Livraison."""
    def setUp(self):
        """Configuration du cas de test pour le service de livraison."""
        pass
    def tearDown(self):
        """Nettoyage après le test de livraison."""
        pass
    def test_effectuerLivraison(self):
        """Test de l'exécution des services de livraison."""
        pass

if __name__ == "__main__":
    unittest.main()

pydoc.writedoc('TestService')