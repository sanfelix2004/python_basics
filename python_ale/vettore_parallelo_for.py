# ESERCIZIO 11
# Scopo: usare due liste parallele (nomi e voti) e stamparle con il for.

nomi = ["Anna", "Marco", "Luca"]
voti = [8, 6, 9]

# Le due liste devono avere la stessa lunghezza
for i in range(len(nomi)):
    # nomi[i] e voti[i] sono collegati perché hanno lo stesso indice
    print("Studente:", nomi[i], "- Voto:", voti[i])