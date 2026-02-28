numeri = [5, 2, 9, 1]

n = len(numeri)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if numeri[j] > numeri[j + 1]:
            temp = numeri[j]
            numeri[j] = numeri[j + 1]
            numeri[j + 1] = temp

print("Lista ordinata:", numeri)