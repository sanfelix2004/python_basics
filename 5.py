# ESERCIZIO 5
# Vettori paralleli: nomi e voti

nomi = []
voti = []

n = int(input("Quanti studenti vuoi inserire? "))

for i in range(n):
    nome = input("Inserisci nome studente: ")
    voto = int(input("Inserisci voto: "))
    nomi.append(nome)
    voti.append(voto)

print("\n--- ELENCO STUDENTI ---")
for i in range(len(nomi)):
    print("Studente:", nomi[i], "- Voto:", voti[i])