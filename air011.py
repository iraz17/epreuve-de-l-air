filin = open("a.txt", "r")
lignes = filin.readlines()
lignes
for ligne in lignes:
    print(ligne)
filin.close()