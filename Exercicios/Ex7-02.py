# Parte 1 - Lendo os dados

#fazer para pokemon


n = int(input("Quantos Pessoas? "))
pessoa = {}
maximo = 0

for i in range(n):
    (nome, cpf, idade) = input().split(" ")
    if not(cpf in pessoa):
        pessoa[cpf] = (nome, idade)

print()
#Obtendo e imprimindo respostas
for (cpf, dados) in pessoa.items():
    print("\n",dados[0], cpf, dados[1])
