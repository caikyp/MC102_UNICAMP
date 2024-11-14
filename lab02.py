###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Escolhendo seu Cartão de Crédito
# Nome: Caiky Pinheiro Foge de Sá
# RA: 204570
###################################################

# Leitura da entrada
x = float(input())
y = float(input())
z = float(input())
k = float(input())

# Cálculos e impressão da saída
e = ((12 * k) < x + 12 * (k - y - (z/100 * k)))
print(e)