n = int(input())
numeros = []
pares = []
impares = []

for i in range(n):
    x = int(input())
    numeros.append(x)

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

pares.sort()

impares.sort(reverse=True)

for i in pares:
    print(i)
    
for i in impares:
    print(i)