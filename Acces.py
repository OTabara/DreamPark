#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi

import pydoc

from Borne_Ticket import Borne_Ticket
from Camera import Camera
from Panneau_Affichage import Panneau_Affichage
import Teleporteur
from Voiture import Voiture


class Acces:
  """"Cette classe représente un accès au parking."""
  def __init__(self):
    """Initialise les attributs de l'accès."""
    self.camera = Camera()
    self.teleporterEntree = Teleporteur.Teleporteur()
    self.teleporterSortie = Teleporteur.Teleporteur()
    self.Borne_Ticket = Borne_Ticket()
    self.Panneau_Affichage = Panneau_Affichage()
  def actionnerCamera(self, client):
    """Active la caméra pour capturer la plaque d'un véhicule entrant."""
    h = self.camera.capturerHauteur(client.getVoiture())
    l = self.camera.capturerLongueur(client.getVoiture())
    im = self.camera.capturerImmatri(client.getVoiture())
    return Voiture(h,l,im)


  def actionnerPanneau(self, parking):
    """cette methode qui met  à jour le panneau d'affichage de l'accès."""
    return self.Panneau_Affichage.afficherNbPlacesDisponibles(parking)

  def recupererChoixServices(self):
      """Simule la récupération des choix de services du client."""
      print("Veuillez sélectionner les services souhaités :")
      print("1. Maintenance")
      print("2. Entretien")
      print("3. Livraison")
      print("Entrez les numéros des services, séparés par des virgules (exemple: 1,3): ")
      choix = input()  # Simule une saisie utilisateur
      return [int(c.strip()) for c in choix.split(",") if c.strip().isdigit()]

  def lancerProcedureEntree(self, client, parking):
    """ la procédure d'entrée d'un véhicule dans le parking."""
    voiture = self.actionnerCamera(client)
    self.Borne_Ticket.recupererInfosCarte(client)
    if client not in parking.listSuperAbonnement:
        place = parking.rechercherPlace(voiture)
        if place == 'Pas de place disponible':
            return "Aucune place disponible pour votre véhicule"
        else :
            if client.estAbonne==True:
                services = self.Borne_Ticket.proposerServices()
                print(f"Services disponibles : {services}")
                choix_services = self.recupererChoixServices()
                print(f"Services choisis par le client : {choix_services}")
            self.Borne_Ticket.delivrerTicket(client, place, parking)
            self.teleporterEntree.teleporterVoiture(client.getVoiture(),place)
    else :
        self.teleporterEntree.teleporterVoitureSuperAbonne(client.getVoiture(),parking)

  def lancerProcedureSortie(self, client, ticket):
      """Procédure de sortie d'un véhicule du parking."""
      # Vérifier la validité du ticket
      if not self.Borne_Ticket.verifierValiditeTicket(ticket):
          return "Ticket invalide. Impossible de sortir."

      # Calculer le montant à payer
      montant_a_payer = self.Borne_Ticket.calculerMontant(ticket)
      print(f"Montant à payer : {montant_a_payer} €")

      # Simuler le paiement
      paiement_effectue = self.Borne_Ticket.effectuerPaiement(montant_a_payer)
      if not paiement_effectue:
          return "Paiement échoué."

      # Libérer la place de parking
      place = ticket.getPlaceAttribuee()
      ticket.getParking().libererPlace(place)

      # Téléporter la voiture vers la sortie
      self.teleporterSortie.teleporterVoiture(client.getVoiture(), place)
      return "Sortie réussie."

pydoc.writedoc('Acces')