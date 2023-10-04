def maior2(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
    
def maior3(n1, n2, n3):
    return maior2(maior2(n1, n2), n3)

result = maior3(1, 10, 5)
print(result)

def achaNum(n, lista):
    if n in lista:
        return True
    else:
        return False
        
print(achaNum(0, [1,2,4,3,5]))

def tem_duplicado(lista):
    for i in lista:
        if lista.count(i) > 1:
            return True
        else:
            return False

print(tem_duplicado([1,1,2,2,3,4,5]))