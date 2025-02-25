#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi
import pydoc
class Borne_Ticket:
 """Cette classe représente une borne de distribution de tickets."""
 def __init__(self):
    """Initialise une instance de la classe Borne_Ticket."""

 def delivrerTicket(self, client, place, parking):
    """cette methode délivre un ticket à l'utilisateur"""
    ticket = (
        f"--- Ticket de Parking ---\n"
        f"Nom du Client : {client.getNom()}\n"
        f"Véhicule : {client.getVoiture().getImmatriculation()}\n"
        f"Place attribuée : {place.getNiveau()}{place.getNumero()}\n"
        f"Prix total : {parking.getPrix()} EUR\n"
        f"Merci d'utiliser nos services."
    )
    print(ticket)
    return ticket
 def proposerServices(self):
   """cette methode propose des services disponibles à l'utilisateur."""
   return ["Entretien", "Maintenance", "Livraison"]
 def proposerAbonnement(self):
   """ cette fonction propose des options d'abonnement à l'utilisateur."""
   pass

 def recupererInfosCarte(self, client):
   """cette fonction récupère les informations de la carte de l'utilisateur."""
   print(f"Récupération des informations de la carte pour {client.getNom()}...")
   #récupération des données
   return "Informations de la carte récupérées avec succès."
 def proposerTypePaiement(self):
   """cette fonction Propose différents types de paiement à l'utilisateur."""
   type_paiement = None
   if not type_paiement:
       type_paiement = input("Type de paiement (Carte/Espece) : ")
   return type_paiement



pydoc.writedoc('Borne_Ticket')