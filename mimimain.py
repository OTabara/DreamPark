from Parking import Parking
from Place import Place
from Client import Client
from Voiture import Voiture
from Acces import Acces

def main():
    # Création du parking avec 10 places et un prix de 5 EUR
    parking = Parking(10, 5.0)

    # Ajout de places au parking
    for i in range(1, 11):
        place = Place(i, "RDC", 5.0, 2.0)
        parking.ajouterPlace(place)

    # Création d'un client et d'une voiture
    voiture = Voiture("AB-123-CD", 4.0, 1.8)
    client = Client("Jean Dupont", "123 Rue de Paris", voiture)

    # Création d'un accès au parking
    acces = Acces(parking)

    # Entrée du client dans le parking
    ticket = acces.lancerProcedureEntree(client)
    print(ticket)

    # Sortie du client du parking
    resultat_sortie = acces.lancerProcedureSortie(client, ticket)
    print(resultat_sortie)

if __name__ == "__main__":
    main()