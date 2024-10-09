def num_itens(s):
    itens = 0
    pos = 0
    while pos != -1:
        itens = itens + 1
        pos = s.find(",",pos+1)
    return itens

s=str(input())
print(num_itens(s))
