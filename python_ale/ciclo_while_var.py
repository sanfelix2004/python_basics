# ESERCIZIO 6
# Scopo: stampare i numeri da 1 a N usando il ciclo while.

n = int(input("Inserisci un numero N: "))

i = 1              # variabile contatore, parte da 1
while i <= n:      # il ciclo continua finché i è minore o uguale a n
    print(i)
    i += 1         # i = i + 1 → importante per evitare ciclo infinito