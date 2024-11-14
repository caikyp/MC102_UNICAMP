###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Geladeiras Subzero
# Nome:
# RA:
###################################################

# leitura de dados
tipo = input()
pessoas = int(input())
potencia = int(input())

# Verificação e impressão do nome do modelo a ser recomendado
if (tipo == "s" or tipo =="S"):
    if (potencia > 130):
        Geladeira = "Frost++"
    else:
        if (pessoas >= 3):
            Geladeira = "DeluxFF"
            if (potencia <= 100):
                Geladeira = "IceCold"
        else:
            if (potencia <= 70):
                Geladeira = "Gel-S"
            else:
                Geladeira = "Gel-SPlus"
if (tipo == "d" or tipo == "D"):
    if (pessoas <= 1):
        Geladeira = "Gel-D"
    elif(pessoas >=4):
        if(potencia < 100):
            Geladeira = "IceCold"
        else:
            Geladeira = "Frost++"
    else:
        if((pessoas == 2 and potencia<=150) or potencia<= 100):
            Geladeira = "Gel-DPlus"
        else:
            Geladeira = "DupCold"

print(Geladeira)
