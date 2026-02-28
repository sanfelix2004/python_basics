# ESERCIZIO 1
# Lista fissa di numeri e stampa di tutti gli elementi

numeri = [3, 6, 1, 0]

print("Lista completa:", numeri)

print("Primo elemento (indice 0):", numeri[0])
print("Secondo elemento (indice 1):", numeri[1])
print("Ultimo elemento (indice 3):", numeri[3])

print("\nStampa di tutti gli elementi uno per riga:")
for i in range(len(numeri)):
    print("Indice", i, "->", numeri[i])