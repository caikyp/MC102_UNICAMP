def main():
    lista = input().split(" ")
    #transforma a lista em inteiros
    lista_int = [int(s) for s in lista]
    i = 1
    for n in lista_int:
        if n == i:
            lista_int[i-1] = 0
        i += 1

    for i in range(len(lista_int)):
        print(lista_int[i])
        print(lista_int[lista_int[i]-1])
        print()
        if lista_int[lista_int[i]-1] == 0:
            lista_int[i] = 0

    for i in range(len(lista_int)):
        if lista_int[lista_int[i]-1] == 0:
            lista_int[i] = 0
    

    print(lista_int)
   

main()

tarefas_possiveis = True
if tarefas_possiveis:
    print("Todas as tarefas podem ser realizadas")
else:
    print("Alguma das tarefas não pode ser realizada")
