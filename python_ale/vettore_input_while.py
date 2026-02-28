# ESERCIZIO 10
# Scopo: stessa cosa dell'esercizio 9 ma con ciclo while.

numeri = []

n = int(input("Quanti numeri vuoi inserire? "))

i = 0
while i < n:
    num = int(input("Inserisci un numero: "))
    numeri.append(num)
    i += 1

print("\nHai inserito questi numeri:")

i = 0
while i < len(numeri):
    print("Indice:", i, "- Valore:", numeri[i])
    i += 1