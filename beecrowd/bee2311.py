n = int(input())
a = dict()


for i in range(n):
    nome = input()
    gd = float(input())
    notas = map(float, input().split())
    
    a["nome"] = nome
    a["gd"] = gd
    a["notas"] = list(notas)

    notaMax = max(a["notas"])
    notaMin = min(a["notas"])
    soma = sum(a["notas"])
    
    nota_final = (soma - notaMin - notaMax) * a["gd"]
    print(f"{a['nome']} {nota_final:.2f}")
        