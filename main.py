#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi

# --- Importations ---
from Abonnement import Abonnement
from Acces import Acces
from Client import Client
from Panneau_Affichage import Panneau_Affichage
from Parking import Parking
from Place import Place
from Voiture import Voiture

# --- Configuration initiale ---
# Créer des véhicules
voiture1 = Voiture(2.0, 4.0, "AB-123-CD")
voiture2 = Voiture(1.8, 4.2, "XY-987-ZT")

# Créer des places de parking
place1 = Place(numero=1, niveau='A', longueur=4.0, hauteur=2.0)
place2 = Place(numero=2, niveau='A', longueur=4.2, hauteur=1.8)

# Créer un parking avec des places disponibles
parking = Parking(nbplace=5, prix=10)
parking.ajouterPlace(place1)
parking.ajouterPlace(place2)

# Créer des clients
client_non_abonne = Client("Youssouf Ali", "1 jkdll", voiture1)
client_abonne = Client("Oumou Tabara", "2 fgdhj", voiture2)
abonnement = Abonnement("Annuelle", 300)
client_abonne.sAbonner(abonnement)

# Ajouter le client abonné à la liste des abonnés du parking
parking.addAbonnement(client_abonne,abonnement)

# Créer un accès au parking
acces = Acces()

# --- Cas 1 : Client non abonné ---
print("---- Cas 1 : Client non abonné ----")
ticket_non_abonne = acces.lancerProcedureEntree(client_non_abonne, parking)
print(ticket_non_abonne)

# --- Cas 2 : Client abonné ---
print("\n---- Cas 2 : Client abonné ----")
ticket_abonne = acces.lancerProcedureEntree(client_abonne, parking)
print(ticket_abonne)

# --- Tests supplémentaires ---
# Vérification des places restantes après les entrées
print("\n--- État du parking ---")
print(acces.Panneau_Affichage.afficherNbPlacesDisponibles(parking))

# --- Sortie du client abonné ---
if ticket_abonne:
    print("\n---- Sortie du client abonné ----")
    resultat_sortie = acces.lancerProcedureSortie(client_abonne, ticket_abonne)
    print(resultat_sortie)
else:
    print("\nPas de ticket généré pour le client abonné.")
