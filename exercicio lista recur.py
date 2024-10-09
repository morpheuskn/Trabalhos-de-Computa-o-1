l=list()
p=list()
l.insert(1,("Atalaia Jurubeba",1,2))
l.insert(2,(3,"Licor de Cacau Xavier",4))
l.insert(3,(5,6,"Biotonico fontora"))
def busca_recur(l,chave):
    if l==[]:
        return False
    if l[0][0]==chave:
        return True
    return busca_recur(l[1:],chave)


def busca(l,chave):
    for i, el in enumerate(l):
        if chave == el:
            return True
    return False

print(busca_recur(l,"Atalaia Jurubeba"))
print(busca(l,"Atalaia Jurubeba"))
p.extend(l[0])
p.extend(l[1])
p.extend(l[2])
print(p)
