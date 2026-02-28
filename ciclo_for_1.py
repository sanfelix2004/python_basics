# FOR con range (usa gli indici)

numeri = []

n = int(input("Quanti numeri vuoi inserire? "))

for i in range(n):
    num = int(input("Inserisci numero: "))
    numeri.append(num)

print("\n--- OUTPUT ---")
for i in range(len(numeri)):
    print("Indice", i, "->", numeri[i])