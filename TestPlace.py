#Auteurs :Youssouf ali rozi et Oumou Tabara Diallo
import unittest
import pydoc
from datetime import datetime, timedelta

from Place import Place
from Placement import Placement
from main import place1


class TestPlace(unittest.TestCase):
    """Test les fonctionnalités de la classe Place"""
    def setUp(self):
        """Configuration du cas de test pour les places de parking."""
        self.placement1 = Placement(datetime.today(), datetime.today() + timedelta(days=1))
        self.placement2 = Placement(datetime.today(), datetime.today() + timedelta(days=1))
        self.place1 = Place(numero=1, niveau='A', longueur=4.0, hauteur=2.0)
        self.place2 = Place(numero=2, niveau='B', longueur=4.2, hauteur=1.8)

    def tearDown(self):
        """Nettoyage après le test de place."""
        self.placement = None
        self.place1 = None
        self.place2 = None
    def test_addPlacementP(self):
        """Test de l'ajout d'un placement à une place de parking."""
        self.place1.addPlacementP(self.placement1)
        self.place2.setEstLibre(False)
        self.place2.addPlacementP(self.placement2)
        self.assertTrue(self.placement1.getEstEncours(), "Le placement n'a pas réussi")
        self.assertFalse(self.placement2.getEstEncours(), "Le placement a réussi")

pydoc.writedoc('TestPlace')
if __name__ == '__main__':
    unittest.main()
