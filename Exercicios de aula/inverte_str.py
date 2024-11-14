def inverte(str,n,str2):
    if n == 0:
        return str2
    str2 = str2 + str[-1]
    return inverte(str[:-1],n-1,str2)
    
s = input()
print(inverte(s,len(s),""))