lista_alunos = []
qt_alunos = int(input("Quantos alunos há na sala? "))

for i in range(qt_alunos): 
    aluno = input()
    lista_alunos.append(aluno)

print(lista_alunos)

lista_notas = []

for i in range(qt_alunos):
    nota = float(input())
    lista_notas.append(nota)

soma = 0
for i in range(len(lista_notas)):
    soma += lista_notas[i]
    lista_notas[i] += 1
    
media = soma / qt_alunos

print("Média =",media)

for i in range(qt_alunos):
    if lista_notas[i] >= 5:
        print(lista_alunos[i])