#Auteurs :Youssouf ali rozi et Oumou Tabara Diallo
import unittest
from datetime import timedelta, datetime
import pydoc
from Placement import Placement


class TestPlacement(unittest.TestCase):
    """Test des fonctionnalités de la classe Placement."""
    def setUp(self):
        """Configuration du cas de test concernant un placement."""
        self.placement = Placement(datetime.today(), datetime.today() + timedelta(days=1))
    def tearDown(self):
        """Nettoyage après le test de placement."""
        self.placement = None

    def test_placement(self):
        """Test de l'ajout d'un placement de voiture."""
        self.assertIsNotNone(self.placement,"le placement n'a pas été créé")

    def test_partirPlace(self):
        """Test de la fonctionnalité de quitter une place parking"""
        pass

pydoc.writedoc('TestPlacement')