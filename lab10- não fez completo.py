###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Kungsleden
# Nome: Caiky Pinheiro Foge de Sá
# RA: 204570
###################################################


def lerMatriz(lin,col):
    matriz = []
    linC = -1
    colC = -1
    for i in range(lin):
        linha = input().split()
        if "C" in linha:
            linC = i
            colC = linha.index("C")
        matriz.append(linha)

    #print(linC,colC)
    #norte
    resp = Andar(matriz,linC-1,colC,lin,col)
    resposta = "N: "+resp
    print(resposta)
    #sul
    resp = Andar(matriz,linC+1,colC,lin,col)
    resposta = "S: "+resp
    print(resposta)
    #leste
    resp = Andar(matriz,linC,colC+1,lin,col)
    resposta = "L: "+resp
    print(resposta)
    #oeste
    resp = Andar(matriz,linC,colC-1,lin,col)
    resposta = "O: "+resp
    print(resposta)
    

def Andar(matriz,lin,col,tamX,tamY):
    listinha = ["Nx","Sx","Lx","Ox","C","F"]
    conta = 0
    while True:
        '''for i in range(len(matriz)):
            print(matriz[i])
        print("")'''
        if lin < 0 or col < 0 or lin == tamX or col == tamY:
            n = "caminho sem saida."
            return n
            break
        elif matriz[lin][col] == "S" or matriz[lin][col] == "Sx":
            matriz[lin][col] = "Sx"
            lin = lin+1
        elif matriz[lin][col] == "N" or matriz[lin][col] == "Nx":
            matriz[lin][col] = "Nx"
            lin = lin-1
        elif matriz[lin][col] == "L" or matriz[lin][col] == "Lx":
            matriz[lin][col] = "Lx"
            col = col+1
        elif matriz[lin][col] == "O" or matriz[lin][col] == "Ox":
            matriz[lin][col] = "Ox"
            col = col-1
        elif matriz[lin][col] == "C":
            n = "de volta a cabana."
            return n
            break
        elif matriz[lin][col] == "F":
            n = "encontrou o fim da floresta."
            return n
            break
        if lin < 0 or col < 0 or lin == tamX or col == tamY:
            n = "caminho sem saida."
            return n
            break
        if matriz[lin][col] in listinha:
            conta = conta + 1
            if conta > 10:
                n = "andou em circulos."
                return n
                break
        
        
linha, coluna = input().split(" ")
linha = int(linha)
coluna = int(coluna)

lerMatriz(linha,coluna)

