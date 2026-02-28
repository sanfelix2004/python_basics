# ESERCIZIO 8
# Città e temperature: trova la città più calda e più fredda

citta = []
temperature = []

n = int(input("Quante città vuoi inserire? "))

for i in range(n):
    nome_citta = input("Inserisci nome città: ")
    temp = float(input("Inserisci temperatura: "))
    citta.append(nome_citta)
    temperature.append(temp)

print("\n--- DATI INSERITI ---")
for i in range(len(citta)):
    print(citta[i], "->", temperature[i], "°C")

# Trova max e min
temp_max = temperature[0]
temp_min = temperature[0]
citta_max = citta[0]
citta_min = citta[0]

for i in range(1, len(temperature)):
    if temperature[i] > temp_max:
        temp_max = temperature[i]
        citta_max = citta[i]
    if temperature[i] < temp_min:
        temp_min = temperature[i]
        citta_min = citta[i]

print("\nCittà più calda:", citta_max, "con", temp_max, "°C")
print("Città più fredda:", citta_min, "con", temp_min, "°C")