# WHILE con condizione di uscita

numeri = []

num = input("Inserisci numero (scrivi STOP per uscire): ")

while num != "STOP":
    numeri.append(int(num))
    num = input("Inserisci numero (scrivi STOP per uscire): ")

print("\n--- OUTPUT ---")
for numero in numeri:
    print(numero)