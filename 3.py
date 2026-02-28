# ESERCIZIO 3
# Somma e media dei numeri inseriti

numeri = []

n = int(input("Quanti numeri vuoi inserire? "))

for i in range(n):
    num = int(input("Inserisci un numero: "))
    numeri.append(num)

# Calcolo somma
somma = 0
for i in range(len(numeri)):
    somma += numeri[i]

media = somma / len(numeri)

print("\nNumeri:", numeri)
print("Somma:", somma)
print("Media:", media)