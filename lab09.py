###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 09 - Álbum de Fotos
# Nome: Caiky Pinheiro Foge de Sá
# RA: 204570
###################################################

def main():
    lista = []
    lista_nome = []
    lista_qtd = []
    f = int(input())

    for i in range(f):
        nomes = input()
        nomes = nomes.split(":")
        nomes[1]=nomes[1][1:]
        if not nomes[1].strip():
            lista.append("")
            continue
        nome = nomes[1].split(", ")
        lista.append(nome)
        for j in nome:
            if j not in lista_nome:
                lista_nome.append(j)
                lista_qtd.append(1)
            else:
                x = lista_nome.index(j)
                lista_qtd[x] = lista_qtd[x] + 1

    maior = max(lista_qtd)
    nomesM = []
    for i in range(len(lista_nome)):
        if lista_qtd[i] == maior:
            nomesM.append(lista_nome[i])
    maiorN = min(nomesM)

    listaD = []
    for i in range(len(lista)):
        if maiorN in lista[i]:
            listaD.append(i+1)
    
        
    print(f"No total, {len(lista_nome)} pessoas apareceram nas fotos.")
    print(f"{maiorN} foi a pessoa mais frequente, aparecendo na(s) foto(s):", *listaD)


main()