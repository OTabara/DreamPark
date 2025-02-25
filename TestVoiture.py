#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi
import pydoc
import unittest
from datetime import datetime, timedelta

from Placement import Placement
from Voiture import Voiture


class TestVoiture(unittest.TestCase):
    """Tests des fonctionnalités de la classe Voiture."""
    def setUp(self):
        """Configuration du cas de test pour le service de voiture."""
        self.voiture1 = Voiture(2.0, 4.0, "AB-123-CD")
        self.voiture2 = Voiture(1.8, 4.2, "XY-987-ZT")
        self.placement = Placement(datetime.today(), datetime.today() + timedelta(days=1))
    def tearDown(self):
        """Nettoyage après le test de voiture."""
        self.voiture1 = self.voiture2 =None
        self.placement = None

    def testVoiture(self):
        """Instanciation d'une voiture."""
        self.assertIsNotNone(self.voiture1,"La voiture n'a pas été instancié")

    def test_addPlacementV(self):
        self.voiture1.addPlacementV(self.placement)
        """Test de l'ajout d'un placement de voiture."""
        self.assertTrue(self.placement, "")


pydoc.writedoc('TestVoiture')