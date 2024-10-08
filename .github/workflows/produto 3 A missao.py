def produtos4():
    tupla = ()
    for n in range(5):
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        preco = float(input("Digite o preço do produto: "))
        tupla += ((produto, quantidade, preco),)
        print (tupla)
    
  
    menos50 = ()
    for produto, quantidade, preco in tupla:
        if quantidade < 50:
            menos50 += (produto,)
    
    if menos50:
        print(f"Produtos com menos de 50 unidades: {menos50}")
    
    maiscaro = tupla[0]
    for i in tupla:
        if i[2] > maiscaro[2]:
            maiscaro = i
    
    produtomaiscaro, n, precomaiscaro = maiscaro
    
    print(f"O produto mais caro é o {produtomaiscaro}, e ele custa {precomaiscaro:.2f} reais")
    
    return tupla

produtos4()
