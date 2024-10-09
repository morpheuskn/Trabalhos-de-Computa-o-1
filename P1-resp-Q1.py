i=int(input())
h=str(input())
q=int(input())
p=float(input())
lotes=q//3
resto%3
if h >="08:00" and h<="09:30":
    if idade<60:
        desconto=0.2
    else:
        desconto=0.3
else:
    desconto=0

total=lotes*3*preço*(1-desconto))+resto*preço
print("Valor de Venda=%.2f" %total)
