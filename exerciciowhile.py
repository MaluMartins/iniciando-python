n = int(input())
indice = 1
soma = 0

while indice <= n:
    
    soma = soma + indice
    
    #depuração
    print("índice: ", indice)
    print("soma parcial = ", soma)
    print("--------------------")
    
    indice = indice + 1
    
print("soma total = ", soma)
    