nomi = []
voti = []

n = int(input("Quanti studenti? "))

for i in range(n):
    nome = input("Nome: ")
    voto = int(input("Voto: "))
    nomi.append(nome)
    voti.append(voto)

# Ordinamento per voto crescente
for i in range(n - 1):
    for j in range(n - 1 - i):
        if voti[j] > voti[j + 1]:
            voti[j], voti[j + 1] = voti[j + 1], voti[j]
            nomi[j], nomi[j + 1] = nomi[j + 1], nomi[j]

print("\nClassifica ordinata:")
for i in range(n):
    print(nomi[i], "-", voti[i])