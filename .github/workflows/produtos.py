def produtos ():
  tupla = []
  for n in range(5):
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input ("Digite o preço do produto: "))
    tupla.append ((produto,quantidade,preco))
    n += 1
  menos50 = [produto for produto, quantidade, n,in tupla if quantidade < 50]
  if menos50:
    print(f"Há {len(menos50)} produtos com menos de 50 unidades: " + "; ".join(menos50))
  maiscaro = tupla[0]
  for i in tupla:
    if i[2] > maiscaro[2]:
      maiscaro = i

  produtomaiscaro, n, precomaiscaro = maiscaro

  print(f"O produto mais caro é o {produtomaiscaro}, e ele custa {precomaiscaro:.2f} reais")

  return tuple(tupla)

produtos()
produtos()