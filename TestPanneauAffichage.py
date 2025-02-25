#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi
import pydoc
import unittest

from Panneau_Affichage import Panneau_Affichage
from Parking import Parking


class TestPanneauAffichage(unittest.TestCase):
    """
    Classe de test unitaire pour `Panneau_Affichage`.
    Cette classe contient des tests pour vérifier la bonne initialisation
    et le comportement des méthodes principales de la classe `Panneau_Affichage`.
    """

    def setUp(self):
        """
        Initialisation des objets nécessaires pour les tests.

        Créé une instance de `Panneau_Affichage` et un objet `Parking`
        avec 2 places disponibles pour tester l'affichage.
        """
        self.Panneau = Panneau_Affichage()
        self.parking = Parking(nbplace=2, prix=10)

    def tearDown(self):
        """
        Nettoyage après chaque test.
        Supprime les instances créées pour garantir que chaque test est
        indépendant des autres.
        """
        self.Panneau = None


    def testPanneauAffichage(self):
        """
        Test de la bonne initialisation de l'objet `Panneau_Affichage`.

        Vérifie que l'objet `Panneau_Affichage` n'est pas `None` après sa création.
        """
        self.assertIsNotNone(self.Panneau)

    def testAfficherNbPlaces(self):
        """
        Test de la méthode `afficherNbPlacesDisponibles`.

        Vérifie que l'affichage du nombre de places disponibles dans le parking
        contient la chaîne attendue, indiquant le nombre de places.
        """
        resultat = self.Panneau.afficherNbPlacesDisponibles(self.parking)
        self.assertIn("Le nombre de places disponibles", resultat)

pydoc.writedoc('TestPanneauAffichage')

