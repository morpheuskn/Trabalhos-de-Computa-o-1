x=int(input())
y=int(input())

def reta(x,y):
    if x==y:
        return 0
    if (x%10)==y:
        return x//10
