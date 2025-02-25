#Auteurs :Youssouf ali rozi et Oumou Tabara Diallo
import pydoc
class Camera:
 """Cette classe représente une caméra utilisée pour capturer
    des données liées à des objets, telles que leur hauteur, leur
    longueur et leur immatriculation """
 def __init__(self):
   """Initialise une nouvelle instance de la classe Camera."""

 def capturerHauteur(self, Voiture):
   """cette methode capture la hauteur d'une voiture"""
   return Voiture.getHauteur()
 def capturerLongueur(self, Voiture):
    """cette methode Capture la longueur d'une voiture."""
    return Voiture.getLongueur()
 def capturerImmatri(self, Voiture):
   """Capture l'immatriculation d'un véhicule."""
   return Voiture.getImmatriculation()


pydoc.writedoc('Camera')