qt_itens = int(input("Digite a quantidade de itens na lista de compras: "))
lista_compras = set()
for i in range(qt_itens):
    item = input()
    lista_compras.add(item)

print(lista_compras)