# ESERCIZIO 4
# Trova il minimo e il massimo in una lista di numeri

numeri = []

n = int(input("Quanti numeri vuoi inserire? "))

for i in range(n):
    num = int(input("Inserisci un numero: "))
    numeri.append(num)

# Assumiamo almeno un numero
minimo = numeri[0]
massimo = numeri[0]

for i in range(1, len(numeri)):
    if numeri[i] < minimo:
        minimo = numeri[i]
    if numeri[i] > massimo:
        massimo = numeri[i]

print("\nNumeri:", numeri)
print("Valore minimo:", minimo)
print("Valore massimo:", massimo)