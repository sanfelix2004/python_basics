# ESERCIZIO 2
# L'utente inserisce N numeri che vengono salvati in una lista

numeri = []

n = int(input("Quanti numeri vuoi inserire? "))

for i in range(n):
    num = int(input("Inserisci un numero: "))
    numeri.append(num)

print("\nHai inserito questi numeri:")
for i in range(len(numeri)):
    print("Indice", i, "->", numeri[i])