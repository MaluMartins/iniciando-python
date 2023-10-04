# definindo a função
def minha_funcao():
    print("ola! essa é uma função")
    

# chamando a função
minha_funcao()

def func_nome(nome):
    print(f"Olá, {nome}! Essa é minha função")
    
func_nome("Malu")
func_nome("João")
func_nome("Maria")

def soma2(num1, num2):
    print(num1 + num2)
    
soma2(2,5)

def soma3(num1, num2, num3 = 0):
    print(num1+num2+num3)
    
soma3(1,2)

# retorno da função: usar o resultado em outras partes do código
def soma2plus(num1,num2):
    return num1+num2

resultado = soma2plus(2,10)

def soma3plus(num1, num2, num3 = 0):
    return soma2plus(num1, num2)+num3

def imprime_lista(lista):
    for i in range(len(lista)):
        print(f"{i}: {lista[i]}")
        
imprime_lista([1,2,3])

def imprime_impar(lista):
    for n in lista:
        if n % 2 != 0:
            print(n)
            
imprime_impar([45,4,6,29,10,23,12,78])


def imprime_indice_par(lista):
    for i in range(len(lista)):
        print(lista[i])
            
def imprime_indice_par2(lista):
    for i in range(0, len(lista), 2):
        if i % 2 == 0:
            print(lista[i])
            
imprime_indice_par([1,3,4,5,7])