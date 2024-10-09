def busca(l,p):
    c=list()
    for el in l:
        if el in p and el not in c:
            c.append(el)
    return c


l=[1,2,3,4,5,6,7,8,9]
p=[2,4,6,8]
print(busca(l,p))
