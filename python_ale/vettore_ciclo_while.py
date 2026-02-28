# ESERCIZIO 8
# Scopo: stessa lista, ma uso il while invece del for.

numeri = [5, 2, 9, 1]

i = 0                          # partiamo dal primo indice (0)
while i < len(numeri):         # l'ultimo indice valido è len(numeri) - 1
    print("Indice:", i, "- Valore:", numeri[i])
    i += 1                     # incremento l'indice per passare all'elemento successivo