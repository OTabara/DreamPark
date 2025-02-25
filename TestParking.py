#Auteurs :Youssouf ali rozi et Oumou Tabara Diallo
import pydoc
import unittest

from Abonnement import Abonnement
from Client import Client
from Parking import Parking
from Place import Place
from Voiture import Voiture
from main import voiture1


class TestParking(unittest.TestCase):
   def setUp(self):
      """initialiser les objets pour les tests"""
      self.parking = Parking(2, 50)
      self.place1 = Place(numero=1, niveau='A', longueur=4.0, hauteur=2.0)
      self.place2 = Place(numero=2, niveau='B', longueur=4.2, hauteur=1.8)
      self.parking.ajouterPlace(self.place1)
      self.parking.ajouterPlace(self.place2)
      self.voiture1 = Voiture(2.0, 4.0, "AB-123-CD")
      self.voiture2 = Voiture(4.0, 6.0, "AB-456-CD")
      self.voiture3 = Voiture(1.8, 4.2, "XY-987-ZT")
      self.client1 = Client("Oumou", "3 Bis Rue Andre",self.voiture1)
      self.client2 = Client("Ali", "6 Chemin du canard", self.voiture2)
      self.abonnement1 = Abonnement("Annuel", 300)
      self.abonnement2 = Abonnement("Annuel", 300)
      self.abonnement2.setEstPackGar(True)

   def tearDown(self):
      """Nettoyage de  l'environnement après chaque test."""
      self.parking = None
      self.voiture1 = None

   def testParking(self):
      self.assertIsNotNone(self.parking)


   def test_rechercherPlace(self):
     """Vérifie la recherche  d'une place disponible."""
     place1 = self.parking.rechercherPlace(self.voiture1)
     place2 = self.parking.rechercherPlace(self.voiture2)
     self.assertNotEqual(place1,'Pas de place disponible')
     self.assertEqual(place2, 'Pas de place disponible')

   def testTrouverPlaceSuperAbonne(self):
      place1 = self.parking.rechercherPlace(self.voiture1)
      place2 = self.parking.rechercherPlace(self.voiture3)
      place3 = self.parking.trouverPlaceSuperAbonne(self.voiture2)
      self.assertNotEqual(place1, 'Pas de place disponible')
      self.assertNotEqual(place2, 'Pas de place disponible')
      self.assertEqual(place3, None)


   def test_NbPlaceslibresParNiveau(self):
      """Teste le calcul du nombre de places libres par niveau."""
      self.assertEqual(self.parking.getPlacesLibres(),2)

   def test_addAbonnement(self):
      """Vérifie l'ajout d'un abonnement."""
      self.parking.addAbonnement(self.client1,self.abonnement1)
      self.assertTrue(self.parking.listAbonnement!=[])
      self.parking.addAbonnement(self.client2,self.abonnement2)
      self.assertTrue(self.parking.listSuperAbonnement != [])




pydoc.writedoc('TestParking')
if __name__ == '__main__':
    unittest.main()
