import sys

def trouver_valeur_unique(lst):
    for i in lst:
        if lst.count(i) == 1:
            return i
    return None

def main():
    try:
        # Récupérer la chaîne à partir des arguments de la ligne de commande
        arguments = sys.argv[1:]
        
        # Vérifier si des arguments ont été fournis
        if not arguments:
            raise IndexError

        # Utiliser la fonction trouver_valeur_unique pour obtenir la valeur unique
        resultat = trouver_valeur_unique(arguments)
        
        # Afficher le résultat
        if resultat is not None:
            print(resultat)
        else:
            print("Aucune valeur unique trouvée.")
    except IndexError:
        print("Veuillez fournir une liste d'arguments.")
        sys.exit(1)

if __name__ == "__main__":
    main()
    