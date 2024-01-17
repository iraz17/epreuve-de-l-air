import sys

def contol_pass_sanitaire(array, string):
    tableau = []
    for element in array:
        if string in element or string.upper() in element:
            tableau.append(element)
    return tableau

def main():
    try:
        # Récupérer la chaîne à partir des arguments de la ligne de commande
        main_str = sys.argv[1:-1]
        sub_str = sys.argv[-1]
    except IndexError:
        print("Veuillez fournir une chaîne en argument.")
        sys.exit(1)

    # Utiliser la fonction contol_pass_sanitaire pour filtrer les éléments du tableau
    result = contol_pass_sanitaire(main_str, sub_str)

    # Afficher les éléments filtrés
    for element in result:
        print(element, end=" ")

if __name__ == "__main__":
    main()
