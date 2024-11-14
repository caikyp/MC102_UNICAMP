N = int(input())

museu = []
for _ in range(N):
    museu.append(list(input()))

M = int(input())
suspeitos = {}
for _ in range(M):
    letra, pistas = input().split()
    suspeitos[letra] = [x for x in pistas.split(",")]


# Verificação da posição do detetive
def find_D(museu):
    linhaD = 0
    colunaD = 0
    for i in museu:
        if "D" in i:
            colunaD = i.index("D")
            return linhaD, colunaD
            break
        linhaD += 1
        
x, y = find_D(museu)

pista = []
lcPoss = []
lcVisited = []
estou = []

lcPoss.append([x,y])
# Coleta das pistas
while len(lcPoss) > 0:
    estou = lcPoss.pop(0)
    x,y = estou
    lcVisited.append(estou)
    
    if museu[x][y].isdigit():
        pista.append(museu[x][y])
    if x-1 >= 0 and museu[x-1][y] != "#":
        lcPoss.append([x-1,y])
    if x+1 <= len(museu)-1 and museu[x+1][y] != "#":
        lcPoss.append([x+1,y])
    if y+1 <= len(museu[x])-1 and museu[x][y+1] != "#":
        lcPoss.append([x,y+1])
    if y-1 >= 0 and museu[x][y-1] != "#":
        lcPoss.append([x,y-1])
    museu[x][y] = "#"

frequencia = {susp: 0 for susp in suspeitos}
for i in pista:
    for letra, numeros in suspeitos.items():
        if i in numeros:
            frequencia[letra] +=1

frequencia = {susp: qtd for susp, qtd in frequencia.items() if qtd != 0}
frequencia = dict(sorted(frequencia.items(), key=lambda item: (-item[1], item[0])))
#saida
resp =""
valor_max = max(frequencia.values())
for letra, num in frequencia.items():
    if num >= valor_max:
        resp = resp + letra + " "

print(resp[:-1])
    
