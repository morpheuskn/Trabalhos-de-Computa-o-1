x=int(input())
y=int(input())

def reta(x,y):
    if x==0:
        return 0
    if (x%10)==y:
        return reta(x//10,y)
    else:
        return reta(x//10,y)*10+x%10
    return
print(reta(x,y))
