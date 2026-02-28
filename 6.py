# ESERCIZIO 6
# Vettori paralleli con analisi: media, promossi, bocciati

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

# Calcolo media
somma = 0
for i in range(len(voti)):
    somma += voti[i]

media = somma / len(voti)

print("\nMedia della classe:", media)

# Promossi e bocciati
print("\nStudenti promossi (voto >= 6):")
for i in range(len(nomi)):
    if voti[i] >= 6:
        print(nomi[i], "-", voti[i])

print("\nStudenti bocciati (voto < 6):")
for i in range(len(nomi)):
    if voti[i] < 6:
        print(nomi[i], "-", voti[i])