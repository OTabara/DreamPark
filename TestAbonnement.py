#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi

import pydoc
import unittest
from datetime import datetime, timedelta

from Abonnement import *
from Contrat import *
from Teleporteur import *


class test_Abonnement(unittest.TestCase):
   def setUp(self):
      """initialiser les objets pour les tests"""
      self.abonnement = Abonnement("Annuel",300)
      self.contrat=Contrat(datetime.today(),datetime.today()+timedelta(days=365))
   def tearDown(self):
      """Nettoyage de  l'environnement après chaque test."""
      self.abonnement = None

   def test_Abonnement(self):
       self.assertIsNotNone(self.abonnement)


   def test_addContrat(self):
      """teste l'ajout d'un contrat associé à un abonnement"""
      self.abonnement.addContrat(self.contrat)
      self.assertFalse(self.abonnement.getContrat()==None)

pydoc.writedoc('TestAbonnement')