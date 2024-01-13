import sys 

def ma_fonction(array_de_strings, separateur):
    string = separateur.join(array_de_strings)
    return string

def main():
    try:
        # Récupérer la chaîne à partir des arguments de la ligne de commande
        main_str = sys.argv[1:-1]  # Exclude the script name and the last argument
        sub_str = sys.argv[-1]
    except IndexError:
        print("Veuillez fournir une chaîne en argument.")
        sys.exit(1)

    # Utiliser la fonction ma_fonction pour découper la chaîne en utilisant des espaces comme séparateurs
    result = ma_fonction(main_str, sub_str)
    
    # Afficher la chaîne résultante
    print(result)

if __name__ == "__main__":
    main()