# ESERCIZIO 14
# Scopo: stessa cosa dell'esercizio 13 ma usando il while.

nomi = []
voti = []

n = int(input("Quanti studenti vuoi inserire? "))

i = 0
while i < n:
    nome = input("Inserisci nome studente: ")
    voto = int(input("Inserisci voto: "))

    nomi.append(nome)
    voti.append(voto)

    i += 1

print("\n--- ELENCO STUDENTI ---")

i = 0
while i < len(nomi):
    print("Studente:", nomi[i], "- Voto:", voti[i])
    i += 1