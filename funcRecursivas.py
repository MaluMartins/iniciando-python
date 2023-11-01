def  soma(n):
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma

print("Soma com repetição: ", soma(10))

# usando função recursiva

def somaR(n):
    if n == 1:
        return 1
    else:
        return n + somaR(n-1) #chamando a si própria
        # 10 + somaR(9) => 10 + (9 + somaR(8))...
    
print("Soma com recursividade: ", somaR(10))

def fibonacci(n):
    if n < 1:
        print('ERRO!')
        elemento = -1
    elif n < 3:
        elemento = 1
    else:
        ultimo = 1
        penultimo = 1
        for i in range(3, n+1):
            elemento = ultimo + penultimo
            penultimo = ultimo
            ultimo = elemento
    return elemento

print("Fibonacci com repetição: ", fibonacci(8))

# usando função recursiva
def fibonacciR(n):
    if n < 1:
        # return "Erro!"
        return -1
    elif n < 3:
        return 1
    else:
        return fibonacciR(n-1) + fibonacciR(n-2)
    
print("Fibonacci com recursividade: ", fibonacciR(8))

def fat(n):
    if n < 0:
        fat = -1
        print('erro')
    elif n == 0:
        fat = 1
    else:
        fat = 1
        for i in range(1,n):
            fat *= i
    return fat

print("Fatorial com repetição: ", fat(5))

def fatR(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n*fatR(n-1)
    
print("Fatorial com recursividade: ", fatR(5))