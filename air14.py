import os
import subprocess

GREEN = '\033[92m'  # Vert
RED = '\033[91m'
RESET = '\033[0m'   # Réinitialiser la couleur

def process_1(args,i,n):
    process = subprocess.Popen(args, stdout=subprocess.PIPE, text=True)
    l = len(args) - 2
    print(f"air0{i} ({n}/{l}) : {GREEN}success{RESET}")
    for _ in range(l):
        output = process.stdout.readline()
        n += 1
        if output:
            output.strip()
            print(f"air0{i} ({n}/{l}) : {GREEN}success{RESET}")
            break
    
        result = process.poll()
        if result is not None:
            print(f"air0{i} ({n}/{l}) : {RED}failed{RESET}")

def process_2(args,i,n):
    process = subprocess.Popen(args, stdout=subprocess.PIPE, text=True)
    l = len(args) - 2
    print(f"air0{i} ({n}/{2}) : {GREEN}success{RESET}")
    for _ in range(l):
        output = process.stdout.readline()
        n += 1
        if output:
            output.strip()
            print(f"air0{i} ({n}/2) : {GREEN}success{RESET}")
            break
    
        result = process.poll()
        if result is not None:
            print(f"air0{i} ({n}/2) : {RED}failed{RESET}")
def main():
    for i in range(1, 14):  # Ajusté la boucle pour commencer à 1
        n = 1
        dossier = f"./air0{i}.py"

        if os.path.exists(dossier):
            
            if dossier == "./air01.py":
                args = ['python3', dossier, 'Bonjour mon gars']
                process_1(args,i,n)
                
            elif dossier == "./air02.py":
                args = ['python3', dossier, 'Crevette magique dans la mer des étoiles', 'la']
                process_2(args,i,n)
            elif dossier == "./air03.py":
                args = ['python3', dossier, "je", "teste", "des", "trucs", " "]
                process_2(args, i,n)
            elif dossier == "./air04.py":
                args = ['python3', dossier, "1 2 3 4 5 4 3 2 1", "bonjour monsieur bonjour"]
                process_1(args, i,n)
            elif dossier == "./air05.py":
                args = ['python3', dossier, "Hello milady,   bien ou quoi ??"]
                process_2(args, i,n)
            elif dossier == "./air06.py":
                args = ['python3', dossier, "1", "2", "3", "4", "5", "+2"]
                process_2(args, i,n)
            elif dossier == "./air07.py":
                args = ['python3', dossier, "Michel", "Albert", "Thérèse", "Benoit", "t"]
                process_2(args, i,n)
            elif dossier == "./air08.py":
                args = ['python3', dossier, "1", "3", "4", "2"]
                process_2(args, i,n)
            elif dossier == "./air09.py":
                args = ['python3', dossier, "10", "20", "30", "fusion", "15", "25", "35"]
                process_2(args, i,n)
            elif dossier == "./air010.py":
                args = ['python3', dossier, "Michel", "Albert", "Thérèse", "Benoit"]
                process_2(args, i,n)
            elif dossier == "./air011.py":
                args = ['python3', dossier, "a.txt"]
                process_2(args, i,n)
            elif dossier == "./air012.py":
                args = ['python3', dossier, "O", "5"]
                process_2(args, i,n)
            elif dossier == "./air013.py":
                args = ['python3', dossier, "6", "5", "4", "3", "2", "1"]
                process_2(args, i,n)
        
        else:
            print(f"air{i:02d} (1/1) : {RED}failed (File not found){RESET}")

if __name__ == "__main__":
    main()
