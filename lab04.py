###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Chefe de Cozinha
# Nome: Caiky Pinheiro Foge de Sá
# RA: 204570
###################################################

# Leitura da entrada
pedidos = 0
hora_minimo = 0
minuto_minimo = 0
teste =  True

horas, minutos, tempo_pedido = [int(x) for x in input().replace(":", " ").split()]

while teste:
    if(horas == 00 and minutos == 00) or (hora_minimo >= 23):
        teste = False
    elif((horas + ((minutos + tempo_pedido) // 60)) < 23):
        if ((hora_minimo*60)+minuto_minimo) <= ((horas*60) + minutos):
            hora_minimo = horas + ((minutos + tempo_pedido)//60)
            minuto_minimo = (minutos + tempo_pedido) % 60  
        elif ((hora_minimo*60)+minuto_minimo) > ((horas*60) + minutos):
            hora_minimo += (minuto_minimo + tempo_pedido)//60
            minuto_minimo = (minuto_minimo + tempo_pedido)%60

        if(hora_minimo < 23):
            pedidos += 1
    horas, minutos, tempo_pedido = [int(x) for x in input().replace(":", " ").split()]
    if(horas>=22) and (minutos>=59):
        teste = False

# Saída de dados
print(pedidos)