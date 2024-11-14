###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 06 - Lista de Compras
# Nome: Caiky Pinheiro Foge de Sá
# RA: 204570
###################################################

d = float(input())
n = int(input())
mercado = []

for i in range(3):
    precos = input().split(" ")
    mercado.append(precos)
    
m1 = []
m2 = []
m3 = []
contagem = 0

for i in range(n):
    x = min(float(mercado[0][i]),float(mercado[1][i]),float(mercado[2][i]))
    if (x <= d):
        d = d-x
        contagem += 1
        if(x == float(mercado[0][i])):
            m1.append(i+1)
        elif(x == float(mercado[1][i])):
            m2.append(i+1)
        else:
            m3.append(i+1)

if(m1 != []):
    print("Itens comprados no PyMarket:")
    print(*m1)
else:
    print("Nenhum item foi comprado no PyMarket")
if(m2 != []):
    print("Itens comprados no ByteBazar:")
    print(*m2)
else:
    print("Nenhum item foi comprado no ByteBazar")
if(m3 != []):
    print("Itens comprados no DevShop:")
    print(*m3)
else:
    print("Nenhum item foi comprado no DevShop")

if(contagem == n):
    print("Foi possível terminar a receita")
else:
    print("Não foi possível terminar a receita")