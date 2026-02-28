nomi = ["Anna", "Marco", "Luca"]
voti = [8, 6, 9]

n = len(voti)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if voti[j] > voti[j + 1]:
            # scambio voti
            voti[j], voti[j + 1] = voti[j + 1], voti[j]
            
            # scambio nomi
            nomi[j], nomi[j + 1] = nomi[j + 1], nomi[j]

print("Classifica ordinata:")
for i in range(n):
    print(nomi[i], "-", voti[i])