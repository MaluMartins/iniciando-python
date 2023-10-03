lista1 = []
lista2 = []
lista_operacoes = []
lista_resultados =[]

for i in range(10):
    x = input("Insira os números da lista 1: ")
    x = int(x)
    lista1.append(x)

for i in range(10):
    y = input("Insira os números da lista 2: ")
    y = int(y)
    lista2.append(y)
    
for i in range(10):
    op = input("Insira os operadores: ")
    lista_operacoes.append(op)

for i in range(10):
    if lista_operacoes[i] == "+":
        r = lista1[i] + lista2[i]
        lista_resultados.append(r)
    elif lista_operacoes[i] == "-":
        r = lista1[i] - lista2[i]
        lista_resultados.append(r)
    elif lista_operacoes[i] == "*":
        r = lista1[i] * lista2[i]
        lista_resultados.append(r)
    elif lista_operacoes[i] == "/":
        r = lista1[i] / lista2[i]
        lista_resultados.append(r)
        
print(lista_resultados)