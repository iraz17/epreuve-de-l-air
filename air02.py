import sys

def ma_fonction(string_a_couper, string_separateur):
    tableau = string_a_couper.split(string_separateur)
    return tableau

def main():
    try:
        # Récupérer la chaîne à partir des arguments de la ligne de commande
        main_str = sys.argv[1]
        sub_str = sys.argv[2]
    except IndexError:
        print("Veuillez fournir une chaîne en argument.")
        sys.exit(1)

    # Utiliser la fonction ma_fonction pour découper la chaîne en utilisant des espaces comme séparateurs
    result = ma_fonction(main_str, sub_str)
    
    # Afficher chaque élément du tableau sur une nouvelle ligne
    for element in result:
        print(element)

if __name__ == "__main__":
    main()
