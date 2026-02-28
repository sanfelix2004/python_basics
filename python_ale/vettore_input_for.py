# ESERCIZIO 9
# Scopo: leggere N numeri da tastiera e salvarli in una lista, poi stamparli.

numeri = []    # lista vuota

n = int(input("Quanti numeri vuoi inserire? "))

# Inserimento nella lista
for i in range(n):
    num = int(input("Inserisci un numero: "))
    # append() aggiunge l'elemento alla fine della lista
    numeri.append(num)

print("\nHai inserito questi numeri:")

for i in range(len(numeri)):
    print("Indice:", i, "- Valore:", numeri[i])