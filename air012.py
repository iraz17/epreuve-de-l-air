import sys

def afficher_escalier(caractere, nb_etages):
    for i in range(1, nb_etages + 1):
        espace = " " * (nb_etages - i)
        bloc = caractere * (2 * i - 1)
        print(espace + bloc)

if __name__ == "__main__":
    try:
        caractere = sys.argv[1]
        nb_etages = int(sys.argv[2])
    except (IndexError, ValueError):
        print("Veuillez fournir un caractère et un nombre d'étages en paramètre.")
        sys.exit(1)

    afficher_escalier(caractere, nb_etages)


