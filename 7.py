# ESERCIZIO 7
# Cerca il voto di uno studente dato il nome

nomi = []
voti = []

n = int(input("Quanti studenti vuoi inserire? "))

for i in range(n):
    nome = input("Inserisci nome studente: ")
    voto = int(input("Inserisci voto: "))
    nomi.append(nome)
    voti.append(voto)

cercato = input("\nInserisci il nome dello studente da cercare: ")

trovato = False
for i in range(len(nomi)):
    if nomi[i] == cercato:
        print("Lo studente", cercato, "ha il voto", voti[i])
        trovato = True
        break

if not trovato:
    print("Studente non trovato.")