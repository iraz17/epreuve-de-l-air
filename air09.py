import sys 

def sorted_fusion(array1, array2):
    result = []
    i, j = 0, 0

    # Fusionner les deux listes en les gardant triées
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1

    # Ajouter les éléments restants des deux listes (s'il y en a)
    result.extend(array1[i:])
    result.extend(array2[j:])

    return result
def main():
    try:
        # Récupérer les listes à partir des arguments de la ligne de commande
        args = sys.argv[1:]
        index_fusion = args.index("fusion")
        array1 = list(map(int, args[:index_fusion]))
        array2 = list(map(int, args[index_fusion + 1:]))

    except ValueError:
        print("Veuillez fournir deux listes d'entiers séparées par 'fusion'.")
        exit(1)

    # Utiliser la fonction sorted_fusion pour fusionner les listes triées
    result = sorted_fusion(array1, array2)

    # Afficher la liste résultante
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
    