import sys 

def tri_rapide(tableau):
    if not tableau:
        return []
    else:
        pivot = tableau[-1]
        plus_petit = [x for x in tableau     if x <  pivot]
        plus_grand = [x for x in tableau[:-1] if x >= pivot]
        return tri_rapide(plus_petit) + [pivot] + tri_rapide(plus_grand)
    

def main():
    try:
        # Récupérer la chaîne à partir des arguments de la ligne de commande
        tableau = sys.argv[1:]
 
    except IndexError:
        print("Veuillez fournir une chaîne en argument.")
        sys.exit(1)

    # Utiliser la fonction contol_pass_sanitaire pour filtrer les éléments du tableau
    result = tri_rapide(tableau)

    # Afficher les éléments filtrés
    for element in result:
        print(element, end=" ")

if __name__ == "__main__":
    main()
