###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 08 - Processamento de Dados
# Nome: Caiky Pinheiro Foge de Sá
# RA: 204570
###################################################

def main():
    n = int(input())
    
    for i in range(n):
        name = input()
        names = Nome(name)
        print(names)
        data = input()
        dtNacs(data)
        endereco = input()
        Endereco(endereco)
        telefone = input()
        Tell(telefone)

def Nome(name):
    name = name.lower()
    name = name.split()
    names = []
    ds = ["de", "do", "dos", "da", "das", "e"]
    for n in name:
        if not n in ds:
            names.append(n.capitalize())
        else:
            names.append(n)
    name = " ".join(names)
    return name
   
def dtNacs(data):
    dia = data[0:2]
    mes = data[2:4] if data[2].isnumeric() else data[3:5]
    ano = data[-4:]
    dtcerta = "{0}-{1}-{2}"
    print(dtcerta.format(dia, mes, ano))

def Endereco(endereco):
    if "-" in endereco:
        endereco = endereco.split(" - ")
    if ", " in endereco:
        endereco = endereco.split(", ")
    endereco[0] = Nome(endereco[0])
    enderecos = "{0}, {1}"
    print(enderecos.format(endereco[0],endereco[1]))
    
def Tell(telefone):
    ddd = telefone[0:2] if telefone[0].isnumeric() else telefone[1:3]
    tell1 = telefone[2:7] if telefone[3].isnumeric() else telefone[4:9]
    tell2 = telefone[-4:]
    tell = "({0}){1}-{2}"
    print(tell.format(ddd,tell1,tell2))
   
   
main()