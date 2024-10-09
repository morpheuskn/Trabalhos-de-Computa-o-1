l1=[3,7,1,90,2]
l2=[3,[98,2,1],10]
print(l1,l2)
def ele(l):
    for el in l:
        print(el)
    return
ele(l1)
ele(l2)

def ele1(l):
    s=0
    for el in l:
        if type(el)==int:
            s+=el
        else:
            s += ele1(el)
    return s

print(ele1(l1))
print(ele1(l2))
