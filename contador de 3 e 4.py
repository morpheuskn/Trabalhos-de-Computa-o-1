x=int(input())

def intv(x):
    if x==0:
        return 0
    if x%10==3 or x%10==4:
        return 1+(intv(x//10))
    return intv(x//10)
    
     

print(intv(x))
    
