n=int(input())
def menorDigito(n):
    if n<10:
        return n
    ret=menorDigito(n//10)
    if n%10<ret:
        return n%10
    return ret

print(menorDigito(n))
