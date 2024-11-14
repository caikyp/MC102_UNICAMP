a = int(input())
b = int(input())
c = int(input())
d = input()

lados = [a, b, c]
lados.sort()

if (lados[0]+lados[1] < lados[2]):
    print("não é triangulo")
else:
    if(lados[0]==lados[1] and lados[0]==lados[2]):
        print("equilatero")
    elif((lados[0]!=lados[1]) and (lados[1]!=lados[2]) and (lados[2]!=lados[0])):
        print("escaleno")
    else:
        print("isosceles")