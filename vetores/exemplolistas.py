# LISTAS
nome_alunos = ["Eduardo", "João", "Leonardo", "Christian", "Miguel"]

# imprimir uma lista
print(nome_alunos)

# iterar sob uma lista
for nome in nome_alunos:
    print("Aluno:", nome)
    
# iterar sob uma lista com while
i = 0

while i < len(nome_alunos):
    print("Aluno", i+1, ":", nome_alunos[i])
    i += 1
    
# imprime o tamamho da lista
print("Lista de tamanho:", len(nome_alunos))

# acessando posições

# acessar a primeira posição
print("Primeiro elemento:",nome_alunos[0])

# acessar a segunda posição
print("Segundo elemento:",nome_alunos[1])

# acessar o último elemento da lista
print("Último elemento:",nome_alunos[-1])

# tres primeiros elementos
print(nome_alunos[0:3])

# tres últimos elementos
print(nome_alunos[-3:])

# a string é uma lista de caracteres
uma_lista_de_nome = "Malu"

for c in uma_lista_de_nome:
    if c == 'u':
        print("Existe!")
        break

# usando in como operador
if 'u' in uma_lista_de_nome:
    print("Existe!")