def Altura(h,c):
    h = h*0.7
    c = c + 1
    if h <= 1:
        return c
    return Altura(h,c)

alt = int(input())

print(Altura(alt,0))