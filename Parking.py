
#Auteurs :Youssouf ali rozi et Oumou Tabara Diallo
import pydoc
class Parking:
 """Cette classe représente un système de parking """

 def __init__(self,nbplace,prix):
    """Initialise une nouvelle instance de la classe Parking."""
    self.nbplace = nbplace
    self.nbPlacesLibres = nbplace
    self.prix = prix
    #self.nbNiveaux = nbNiveaux
    self.collectionPlaceDispo = []
    self.listAbonnement = []
    self.listSuperAbonnement = []
    # Ajouter la liste des voitures des superaAbonné n'ayant pas eu de place
    self.parkingSuperAbonnes = [] # placer quand meme les voiture des superaAbonné quelque part


 def getPlacesLibres(self):
     return self.nbPlacesLibres
 def setPlacesLibres(self,nbPlace):
     self.nbPlacesLibres = nbPlace
 def getPrix(self):
     return self.prix

 def ajouterPlace(self, place):
     self.collectionPlaceDispo.append(place)

 def rechercherPlace(self, V):
   """Recherche une place de parking disponible."""
   for p in self.collectionPlaceDispo :
      if (p.getHauteur() >= V.getHauteur() and p.getLongueur() >= V.getLongueur()):
          self.collectionPlaceDispo.remove(p)  # Réserve la place
          self.nbPlacesLibres -= 1  # Met à jour le nombre de places libres
          return p
   return 'Pas de place disponible'

 def trouverPlaceSuperAbonne(self, V):
    """trouve une place de parking disponible pour les super abonnés."""
    place = self.rechercherPlace(V)
    if place != 'Pas de place disponible':
        return place
    else:
        return None
           
 def NbPlaceslibresParNiveau(self):
     """cette methode retourne le nombre de places libres par niveau."""
     return self.nbPlacesLibres

 def addAbonnement(self,client, abonnement):
    """ajoute un abonnement pour un utilisateur."""
    if abonnement.getEstPackGar() :
        self.listSuperAbonnement.append(client)
    else :
        self.listAbonnement.append(client)






pydoc.writedoc('Parking')