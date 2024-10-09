def num_itens(s):
    itens = 0
    pos = 0
    while pos != -1:
        itens = itens + 1
        pos = s.find(",",pos+1)
    return itens



def obtem_item(s,n): # testa se o numero do item é válido
    if n < 0 or n > num_itens(s) - 1:
        return ""
# procura a "," antes do item
    item = 0
    ini = 0
    while item != n:
        ini = s.find(",",ini) + 1 # posicao depois da ","
        item = item + 1
# procura a "," depois do item
    fim = s.find(",",ini)
    if fim == -1:        # ultimo item
        return s[ini:]
    else:
        return s[ini:fim]

s=str(input())

n=int(input())

print(obtem_item(s,n))
print(num_itens(s))

