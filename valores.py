a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

totalPar = 0
totalImpar = 0
totalPositivo = 0
totalNegativo = 0

#verificação dos pares
if a % 2 == 0:
    totalPar = totalPar +1
if b % 2 == 0:
    totalPar = totalPar +1
if c % 2 == 0:
    totalPar = totalPar +1
if d % 2 == 0:
    totalPar = totalPar +1
if e % 2 == 0:
    totalPar = totalPar +1

#verificação dos ímpares
if a % 2 != 0:
    totalImpar = totalImpar +1
if b % 2 != 0:
    totalImpar = totalImpar +1
if c % 2 != 0:
    totalImpar = totalImpar +1
if d % 2 != 0:
    totalImpar = totalImpar +1
if e % 2 != 0:
    totalImpar = totalImpar +1

#verificação dos positivos
if a > 0:
    totalPositivo = totalPositivo +1
if b > 0:
    totalPositivo = totalPositivo +1
if c > 0:
    totalPositivo = totalPositivo +1
if d > 0:
    totalPositivo = totalPositivo +1
if e > 0:
    totalPositivo = totalPositivo +1

#verificação dos negativos
if a < 0:
    totalNegativo = totalNegativo +1
if b < 0:
    totalNegativo = totalNegativo +1
if c < 0:
    totalNegativo = totalNegativo +1
if d < 0:
    totalNegativo = totalNegativo +1
if e < 0:
    totalNegativo = totalNegativo +1

print(totalPar,"valor(es) par(es)") 
print(totalImpar, "valor(es) impar(es)") 
print(totalPositivo, "valor(es) positivo(s)") 
print(totalNegativo,"valor(es) negativo(s)")