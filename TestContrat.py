#Auteurs :Youssouf ali rozi et Oumou Tabara Diallo
import pydoc
import unittest
from datetime import timedelta, datetime

from Abonnement import *
from Acces import *
from Borne_Ticket import *
from Camera import *
from Contrat import *
from Panneau_Affichage import *
from Parking import *
from Teleporteur import *
class TestContrat(unittest.TestCase):
   def setUp(self):
      """initialiser les objets pour les tests"""
      self.contrat = Contrat(datetime.today(),datetime.today()+timedelta(days=365))
   def tearDown(self):
      """Nettoyage de  l'environnement après chaque test."""
      self.contrat = None
   def test_Contrat(self):
       self.assertIsNotNone(self.contrat)

   def test_rompreContrat(self):
      """Vérifie la rupture d'un contrat."""
      self.contrat.rompreContrat()
      self.assertFalse(self.contrat.getEstEncours())

pydoc.writedoc('TestContrat')