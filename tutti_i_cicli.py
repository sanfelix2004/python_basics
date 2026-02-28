# Programma completo

numeri = []

n = int(input("Quanti numeri vuoi inserire? "))

# FOR per inserimento
for i in range(n):
    num = int(input("Inserisci numero: "))
    numeri.append(num)

print("\nLista completa:", numeri)

# FOR con indice
print("\nFOR con indice:")
for i in range(len(numeri)):
    print("Indice", i, "->", numeri[i])

# FOR diretto
print("\nFOR diretto:")
for numero in numeri:
    print(numero)

# WHILE
print("\nWHILE:")
i = 0
while i < len(numeri):
    print(numeri[i])
    i += 1