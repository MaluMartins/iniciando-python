o = input()
matriz = []

soma = 0
lista = []

for i in range(12):
    m = []
    for j in range(12):
        m.append(float(input()))
    matriz.append(m)

for i in range(12):
    for j in range(12):
        if j > i:
            lista.append(matriz[i][j])

for n in lista:
    soma = soma + n
    media = soma/len(lista)
    
if o == "s":
    print(f"{soma:.1f}")
elif o == "m":
    print(f"{media:.1f}")
