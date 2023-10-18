import random

def criar_campo(x, y):
    campo = []
    
    # criando a matriz do campo a partir de x (qt de linhas) e y (qt de colunas)
    for i in range(x):
        linha = []
        for j in range(y):
            linha.append('.')
        campo.append(linha)
            
    return campo

def imprime_campo(campo):
    for i in range(len(campo)):
        for j in range(len(campo[0])):
            print(campo[i][j], end="")
        
        print()

        
def criar_bombas(campo, n_bombas):
    random.seed()

    for i in range(n_bombas):
        a = random.randint(0, (len(campo)-1))
        b = random.randint(0, (len(campo[0])-1))
        campo[a][b] = "#"
                
    return campo

def imprime_campo_jogo(campo):
    for i in range(len(campo)):
        for j in range(len(campo[0])):
            if campo[i][j] == "#":
                print(".", end="")
            else:
                print(campo[i][j], end="")
        
        print()
                
def criar_jogo(x, y, n_bombas):
    campo = criar_campo(x,y)
    campo_com_bombas = criar_bombas(campo, n_bombas)
    
    return campo_com_bombas

def jogar(campo, n_jogadas):
    for n in range(n_jogadas):
        imprime_campo_jogo(campo)
        
        i, j = input("Digite a posição (i,j): ").split()
        i = int(i)
        j = int(j)
        
        if campo[i][j] == "P":
            continue
        
        if campo[i][j] == "#":
            print("BOOM! Game Over!")
            return
        
        campo[i][j] = 'P'
        
    print("You Win!")

jogo = criar_jogo(5,5,5)

jogar(jogo, 5)