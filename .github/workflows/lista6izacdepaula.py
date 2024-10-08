def livros1 (tupla1,tupla2,tupla3,tupla4):
  resultado = (tupla1 + tupla2 + tupla3 + tupla4)
  return resultado
#print (livros1 ( ('Mistborn',), ('Brandon Sanderson',), (766,), (2006,) ))
#print (livros1 ( ('Mistborn', 'Percy Jackson'), ('Brandon Sanderson', 'Rick Riordan'), (766, 377),(2006, 2005)))
#print (livros1 ( ('Mistborn', 'Percy Jackson', 'A Arma Escarlate'), ('Brandon Sanderson', 'Rick Riordan', 'Renata Ventura'), (766, 377, 667), (2006, 2005, 2012)))


def posicao2 (latitudes, longitudes, sensores, sensor):
    localizacao = []
    for i in range(len(sensores)):
        if sensores[i] == sensor:
            localizacao.append((latitudes[i], longitudes[i]))
    return tuple(localizacao)
#print (posicao2 ( (1.0, 3.4, -3.2), (5.6, 10.2, 20.1), ('S1', 'S2', 'S1'), 'S1' ))
#print (posicao2 ( (1.0, 3.4, -3.2), (5.6, 10.2, 20.1), ('S1', 'S2', 'S1'), 'S2' ))
#print (posicao2 ( (1.0, 3.4, -3.2), (5.6, 10.2, 20.1), ('S1', 'S2', 'S1'), 'S3' ))
#print (posicao2 ( (7.77, 1.54, -9.82, 22.38, -17.43), (11.27, -42.39, -28.75, -31.15, 37.44), ('S3', 'S1', 'S4', 'S4', 'S2'), 'S4' ))


def substituicao3 (frase, original, substituta):
    resultado = ""
    lenoriginal = len(original)
    lenfrase = len(frase)
    i = 0
    while i < lenfrase:
        if frase[i:i+lenoriginal] == original:
            resultado += substituta
            i += lenoriginal
        else:
            resultado += frase[i]
            i += 1  
    return resultado
#print(substituicao3 ('Este eh um teste.', 'um', 'o'))
#print(substituicao3 ('Este eh um teste.', 'te', 'aeiou'))
#print(substituicao3 ('aaaa', 'aa', 'b'))
#print(substituicao3 ('áááá', 'aa', 'b'))
#print(substituicao3 ('aaaa', 'aaaaaaaa', 'b'))
#print(substituicao3 ('DDdDDdddD', 'dD', ' StrINGtesTE'))
#print(substituicao3 ('Saida esta incorreta!', 'in', ''))
#print(substituicao3 ('Retorno errado?', 'errado', 'certo'))


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
