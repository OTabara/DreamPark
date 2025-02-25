#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi
import unittest
import pydoc

from Borne_Ticket import Borne_Ticket
from Client import Client
from Parking import Parking
from Place import Place
from Voiture import Voiture


class TestBorneTicket(unittest.TestCase):

   def setUp(self):
      """initialiser les objets pour les tests"""
      self.borne = Borne_Ticket()
      self.voiture1 = Voiture(1.8, 4.2, "XY-987-ZT")
      self.client1 = Client("Ali", "6 chemin edgard varese", self.voiture1)
      self.parking = Parking(2, 50)
      self.place1 = Place(numero=2, niveau='B', longueur=4.2, hauteur=1.8)
      self.parking.ajouterPlace(self.place1)

   def tearDown(self):
      """Nettoyage de  l'environnement après chaque test."""
      self.borne = None

   def testBorneTicket(self):
       self.assertIsNotNone(self.borne)

   def test_delivrerTicket(self):
      """Vérifie la délivrance d'un ticket."""
      ticket = self.borne.delivrerTicket(self.client1,self.place1, self.parking)
      self.assertIn('Ticket de Parking', ticket)

   def test_proposerServices(self):
     """Teste l'affichage des services proposés par la borne."""
     pass
   def test_proposerAbonnement(self):
     """Vérifie la proposition d'abonnement par la borne."""
     pass
   def test_recupererInfosCarte(self):
     """Vérifie la récupération des informations de la carte."""
     pass
   def test_proposerTypePaiement(self):
     """Teste les types de paiement proposés par la borne."""
     pass


pydoc.writedoc('TestBorneTicket')

if __name__ == '__main__':
    unittest.main()
