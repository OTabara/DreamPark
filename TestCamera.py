#Auteurs :Youssouf ali rozi et Oumou Tabara Diallo
import pydoc
import unittest
from Camera import Camera
from Voiture import Voiture
class test_Camera(unittest.TestCase):
   def setUp(self):
      """initialiser les objets pour les tests"""
      self.camera = Camera()
      self.voiture = Voiture(2.0, 4.0, "AB-123-CD")
   def tearDown(self):
      """Nettoyage de  l'environnement après chaque test."""
      self.camera = None

   def tesCamera(self):
     """Vérifie que l'objet camera est bien instanciée."""
     self.assertIsNotNone(self.camera)

   def test_capturerHauteur(self):
     """Vérifie la capture  de la hauteur du véhicule."""
     hauteur = self.camera.capturerHauteur(self.voiture)
     self.assertEqual(hauteur, 2.0, "La hauteur capturée est incorrecte.")
   def test_capturerLongueur(self):
    """Vérifie la capture de la longueur du véhicule."""
    longueur = self.camera.capturerLongueur(self.voiture)
    self.assertEqual(longueur, 4.0, "La longueur capturée est incorrecte.")
   def test_capturerImmatri(self):
     """Vérifie la capture de l'immatriculation du véhicule."""
     immatri = self.camera.capturerImmatri(self.voiture)
     self.assertEqual(immatri, "AB-123-CD", "L'immatriculation capturée est incorrecte.")
pydoc.writedoc('TestCamera')
if __name__ == '__main__':
    unittest.main()