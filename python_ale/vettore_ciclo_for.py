# ESERCIZIO 7
# Scopo: avere una lista fissa di numeri e stamparli con il for.

numeri = [5, 2, 9, 1]   # lista di 4 elementi

# len(numeri) restituisce la lunghezza della lista (qui 4)
for i in range(len(numeri)):
    # i è l'indice, numeri[i] è il valore in quella posizione
    print("Indice:", i, "- Valore:", numeri[i])