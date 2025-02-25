#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi

import pydoc
import unittest

from Abonnement import Abonnement
from Acces import Acces
from Parking import Parking
from Place import Place
from Voiture import Voiture
from Client import Client


class test_Acces(unittest.TestCase):
    def setUp(self):
        """initialiser les objets pour les tests"""
        self.acces = Acces()

        self.voiture1 = Voiture(2.0, 4.0, "AB-123-CD")
        self.voiture2 = Voiture(2.0, 4.5, "XY-456-EF")
        self.voiture3 = Voiture(1.6, 3.9, "GH-789-IJ")
        self.place1 = Place(numero=1, niveau='A', longueur=4.0, hauteur=2.0)
        self.place2 = Place(numero=1, niveau='A', longueur=4.5, hauteur=2.0)
        self.parking = Parking(nbplace=2, prix=10)
        self.parking.ajouterPlace(self.place1)
        self.parking.ajouterPlace(self.place2)
        self.abonnement1 = Abonnement("Annuelle", 300)
        self.abonnement2 = Abonnement("Annuelle", 350)
        self.abonnement2.setEstPackGar(True)
        self.client1 = Client("youssouf ali", "6 chemin de edgard varese", self.voiture1)
        self.client1.sAbonner(self.abonnement1)
        #Supers Abonnés
        self.client2 = Client("ali ", "25 avenue des Champs, Lyon", self.voiture2)
        self.client2.sAbonner(self.abonnement2)
        self.client3 = Client("tabara", "50 boulevard Haussmann, Lyon", self.voiture3)
        self.client3.sAbonner(self.abonnement2)

        self.parking.addAbonnement(self.client1, self.abonnement1)
        self.parking.addAbonnement(self.client2, self.abonnement2)
        self.parking.addAbonnement(self.client2, self.abonnement2)

    def tearDown(self):
        """Nettoyage de  l'environnement après chaque test."""
        self.acces = None

    def testAccess(self):
        """teste si l'accès est correctement initialisé."""
        self.assertIsNotNone(self.acces)

    def test_actionnerCamera(self):
        """teste d'activation de camera"""
        res = self.acces.actionnerCamera(self.client1)
        self.assertEqual(res.getImmatriculation(), self.client1.getVoiture().getImmatriculation())

    def test_actionnerPanneau(self):
        """teste si le panneau d'affichage de l'accès est à jour ."""
        res = self.acces.actionnerPanneau(self.parking)
        res_attendu = "Le nombre de places disponibles est : 2"
        self.assertEqual(res,res_attendu)

    def test_lancerProcedureEntree(self):
        """Verifie la procédure d'entrée d'un véhicule dans le parking."""
        self.acces.lancerProcedureEntree(self.client1,self.parking)
        self.assertIsNotNone(self.client1.getVoiture().getPlacementV())

        #self.acces.lancerProcedureEntree(self.client2,self.parking)
        #self.assertIsNotNone(self.client2.getVoiture().getPlacementV())

        #self.acces.lancerProcedureEntree(self.client3,self.parking)
        #self.assertIsNone(self.client2.getVoiture().getPlacementV())





pydoc.writedoc('TestAcces')
if __name__ == '__main__':
    unittest.main()