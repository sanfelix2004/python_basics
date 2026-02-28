# WHILE con contatore manuale

numeri = []

n = int(input("Quanti numeri vuoi inserire? "))

i = 0
while i < n:
    num = int(input("Inserisci numero: "))
    numeri.append(num)
    i += 1

print("\n--- OUTPUT ---")

i = 0
while i < len(numeri):
    print("Indice", i, "->", numeri[i])
    i += 1