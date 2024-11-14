###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Tit for Tat
# Nome: Caiky Pinheiro Foge de Sá
# RA: 204570
###################################################

# Leitura da entrada
k = int(input())
lista = []
pnt_1 = 0
pnt_2 = 0
listaresp = [0]

for i in range(k):
    pronunciamento = int(input())
    lista.append(pronunciamento)

# Processamento dos dados
for j in lista[0:k-1]:
    if j == 0:
        listaresp.append(0)
    else:
        listaresp.append(1)

for k in range(k):
    if(lista[k] == listaresp[k]):
        if (lista[k] == 0):
            pnt_1 += 3 
            pnt_2 += 3 
        if (lista[k] == 1):
            pnt_1 += 1 
            pnt_2 += 1 
    else:
        if (lista[k] == 1) and (listaresp[k] == 0):
            pnt_1 += 5
        if (lista[k] == 0) and (listaresp[k] == 1):
            pnt_2 += 5
    print(listaresp[k])

# Saída de dados
print(pnt_2)
print(pnt_1)
