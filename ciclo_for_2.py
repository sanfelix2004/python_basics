# FOR diretto (scorre direttamente i valori)

numeri = []

n = int(input("Quanti numeri vuoi inserire? "))

for i in range(n):
    num = int(input("Inserisci numero: "))
    numeri.append(num)

print("\n--- OUTPUT ---")
for numero in numeri:
    print("Valore:", numero)