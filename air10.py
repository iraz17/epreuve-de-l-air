import sys

def ma_rotation(array):
    tableau = []
    for i in range(len(array)):
        tableau.append(array[i-1])

    return tableau
def main():
    try:
        # Récupérer la chaîne à partir des arguments de la ligne de commande
        array = sys.argv[1:]
 
    except IndexError:
        print("Veuillez fournir une chaîne en argument.")
        sys.exit(1)

    # Utiliser la fonction contol_pass_sanitaire pour filtrer les éléments du tableau
    result = ma_rotation(array)

    # Afficher les éléments filtrés
    for element in result:
        print(element, end=" ")

if __name__ == "__main__":
    main()
