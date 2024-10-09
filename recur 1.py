n=int(input(">>> "))
def fat(n):
    print("N = %d" %n)
    if n < 2:
        return 1
    else:
        return n*fat(n-1)

print(fat(n))
