# ESERCIZIO 13
# Scopo: leggere da tastiera nomi e voti, salvarli in vettori paralleli e stamparli.

nomi = []
voti = []

n = int(input("Quanti studenti vuoi inserire? "))

# Inserimento dati
for i in range(n):
    nome = input("Inserisci nome studente: ")
    voto = int(input("Inserisci voto: "))
    
    # Aggiungo alla fine delle due liste nello stesso ordine
    nomi.append(nome)
    voti.append(voto)

print("\n--- ELENCO STUDENTI ---")
for i in range(len(nomi)):
    print("Studente:", nomi[i], "- Voto:", voti[i])