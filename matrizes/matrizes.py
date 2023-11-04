m = [
    [10, 35, 2, 5, 9],
    [1, 2, 7, 5, 2],
    [9, 5, 5, 1, 3],
    [2, 4, 6, 5, 1],
    [1, 2, 3, 7, 6]
]

# imprime todos os elementos da matriz
for i in range(5):
    for j in range(5):
        print(m[i][j])
        
print("---------------")

# imprimir todos os elmentos da coluna 0 da matiz
for i in range(5):
    print(m[i][0])
    
print("---------------")
    
# imprimir todos os elementos da linha 2 da matriz
for j in range(5):
    print(m[2][j])
    
print("---------------")

# imprimir todos os elementos pares da matriz PROVA!!!
for i in range(5):
    for j in range(5):
        if m[i][j] % 2 == 0:
            print(m[i][j])

print("---------------")
            
# imprimir todos os elementos em linhas pares na matriz
for i in range(5):
    for j in range(5):
        if i % 2 == 0:
            print(m[i][j])

# ou

for i in range(0, 5, 2):
    for j in range(5):
        print(m[i][j])

print("---------------")

# imprimir todos os elementos em colunas impar
for j in range(5):
    for i in range(5):
        if j % 2 != 0:
            print(m[i][j])

print("---------------")

# imprimir todos os elementos da diagonal principal
for j in range(5):
    for i in range(5):
        if i == j:
            print(m[i][j])

# ou

for n in range(5):
    print(m[n][n])
            
print("---------------")

# imprimir todos os elementos da diagonal secundária
for j in range(5):
    for i in range(5):
        if i + j == 4:
            print(m[i][j])
            
# ou

for i in range(5):
    print(m[i][(5-i)-1])
