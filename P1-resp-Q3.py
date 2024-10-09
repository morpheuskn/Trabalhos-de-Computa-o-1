n=int(input())
def geraSequencia(n):
    print(n)
    if n==1:
        return
    if n%2==0:
        geraSequencia(n//2)
    else:
        geraSequencia(3*n+1)
    return

print(geraSequencia(n))
