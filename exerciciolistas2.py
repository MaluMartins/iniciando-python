# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

notas = []

for i in range(5):
    nota = int(input())
    notas.append(nota)
    
# Mostre a quantidade de valores que foram lidos;
print("A quantidade de valores lidos é:", len(notas))

# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print(notas)

# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
notas.reverse()
print(notas)

# Calcule e mostre a soma dos valores;
notas.reverse()
print(notas)

soma = 0

for i in notas:
    soma = soma + i

print("A soma dos valores é:", soma)

# Calcule e mostre a média dos valores;
media = soma/5
print("A média é:", media)

# Calcule e mostre a quantidade de valores acima da média calculada;
acima_media = []

for i in notas:
    if i > media:
        acima_media.append(i)
        
print("A quantidade de valores acima da média é:", len(acima_media))

# Calcule e mostre a quantidade de valores abaixo de sete;
abaixo_de_7 = []

for i in notas:
    if i > media:
        abaixo_de_7.append(i)

print("A quantidade de valores abaixo de 7 é:", len(abaixo_de_7))

print("fim")