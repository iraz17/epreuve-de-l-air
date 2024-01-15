import sys

def ma_fonction(argument, operateur):
    argg = list(map(int, argument))
    op = int(operateur[1])
    result = []
    for i in range(len(argument)):
        if operateur[0] == "+":
            number = argg[i] + op
        elif operateur[0] == "-":
            number = argg[i] - op
        else:
            break
        result.append(number)
    return result
def main():
    try:
        # Récupérer la chaîne à partir des arguments de la ligne de commande
        main_str = sys.argv[1:-1]
        sub_str = sys.argv[-1]
    except IndexError:
        print("Veuillez fournir une chaîne en argument.")
        sys.exit(1)

    # Utiliser la fonction ma_fonction pour découper la chaîne en utilisant des espaces comme séparateurs
    result = ma_fonction(main_str, sub_str)

    for element in result:
        print(element, end=" ")

if __name__ == "__main__":
    main()
