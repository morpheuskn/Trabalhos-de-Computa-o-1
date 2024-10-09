x=int(input())

def mult(x):
    if x<10:
        return x
    else:
        return 1+mult(x//10)

print(mult(x))
    
