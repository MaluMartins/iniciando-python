aluno = {
    "nome": "Malu",
    "idade": 18,
    "telefone": "1699999999",
    "notas": [2.0, 7.6, 8.4, 10.0]
}

# imprima todas as notas do aluno
print(aluno["notas"])

#imprima a terceira nota do aluno
print(aluno["notas"][2])

print(aluno["nome"])

# dicionario vazio
d = dict()
d["titulo"] = "IPE"
d["horario"] = "19:30"

print(d)

# imprimir na tela todas as chaves do dicionario

print(aluno.keys()) # cria uma lista das chaves do dicionario

for k in aluno.keys():
    print(aluno[k]) #imprimindo todos os valores das chaves