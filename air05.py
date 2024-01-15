import sys

import sys

def remove_adjacent_duplicates(s):
    result = [s[0]]

    for char in s[1:]:
        if char != result[-1]:
            result.append(char)

    return ''.join(result)

def main():
    try:
        # Récupérer la chaîne à partir des arguments de la ligne de commande
        arguments = ' '.join(sys.argv[1:])

        # Vérifier si des arguments ont été fournis
        if not arguments:
            raise IndexError

        # Utiliser la fonction pour supprimer les caractères identiques adjacents
        resultat = remove_adjacent_duplicates(arguments)
        print(resultat)
    except IndexError:
        print("Veuillez fournir une chaîne d'arguments.")
        sys.exit(1)

if __name__ == "__main__":
    main()