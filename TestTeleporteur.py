#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi
import pydoc
import unittest

from Parking import Parking
from Place import Place
from Teleporteur import Teleporteur
from Voiture import Voiture


class test_Teleporteur(unittest.TestCase):
   def setUp(self):
      """initialiser les objets pour les tests"""
      self.teleporteur = Teleporteur()
      self.parking = Parking(nbplace=1, prix=10)
      self.place1 = Place(numero=1, niveau='A', longueur=4.0, hauteur=2.0)
      self.parking.ajouterPlace(self.place1)
      self.voiture1 = Voiture(2.0, 4.0, "AB-123-CD")
      self.voiture2 = Voiture(1.8, 4.2, "XY-987-ZT")


   def tearDown(self):
      """Nettoyage de  l'environnement après chaque test."""
      self.teleporteur = None

   def test_teleporterVoiture(self):
        """Vérifie la téléportation d'une voiture est bien faite."""
        resultat = self.teleporteur.teleporterVoiture(self.voiture1,self.place1)
        self.assertIsNotNone(resultat, "La methode doit retourner un resultat")
        self.assertEqual(resultat, self.voiture1.getPlacementV())
        self.assertEqual(resultat, self.place1.getPlacementP())


   def test_teleporterVoitureSuperAbonne(self):
        """Vérifie la téléportation de la voiture du super abonnement est bien effectuée."""

        res1 = self.teleporteur.teleporterVoitureSuperAbonne(self.voiture1,self.parking)
        #Plus de place disponible donc on ajoute la voiture dans la liste de parking spéciale
        res2 = self.teleporteur.teleporterVoitureSuperAbonne(self.voiture2,self.parking)
        self.assertEqual(res1, self.voiture1.getPlacementV())
        self.assertEqual(res2, None)

pydoc.writedoc('TestTeleporteur')