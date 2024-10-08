def meio1 (lista,n1,n2):
  quanto = 0
  for n in lista:
    if (n <= n1 and n >= n2) or (n <= n2 and n >= n1):
     quanto += 1
  return (quanto)
#print (meio1([-1,0,1,1.2,3,4.5,4.9,5.1,6,7,8],1,5))
#print (meio1([1,7,1.2,3,8,6,4.9,5.1,4.5],10,50))
#print (meio1([0,0,0,0,0,0,0,0],0,0))
#print (meio1([-1,0.1,-1.2,4,10,2],-2,10))


def produto2 (lista):
  n = 1
  for numero in lista:
    if (type(numero) == int) or (type(numero) == float):
      n *= numero
  return n
#print (produto2([4,2,3]))
#print (produto2([4,2,3,1,2,0]))
#print (produto2([1.5,2,1j,2,3.5,'100']))
#print (produto2([True,1.1,2,1j,2.2,3.2]))


def valor3 (n):
  if n == 0:
    return 0
  else:
    saida = 0
    for i in range (1, n+1):
      saida += 1/(i * 2)
    return saida
#print (valor3(0))
#print (valor3(1))
#print (valor3(2))
#print (valor3(4))


def comparacao4 (lista1,lista2):
  n1 = len(lista1)
  n2 = len(lista2)
  saida = []
  if n1 != n2:
    return []
  else:
    for i in range (n1):
      if lista1[i] > lista2[i]:
        saida.append(lista1[i])
      elif lista2[i] > lista1[i]:
        saida.append(lista2[i])
    return saida
#print(comparacao4([3,6,7,7,9],[4,6,4,8,5]))
#print(comparacao4([8,2,5,5,7,8],[7,2,7,4,9,10]))
#print(comparacao4([3,3,10,3,3,3,4],[2,1,7,10,4,1,8]))


def tabuada5 (n):
  saida = []
  for i in range (1,10+1):
    saida.append (n * i)
  return saida
#print (tabuada5((-1)))
#print (tabuada5((4)))
#print (tabuada5((9)))
#print (tabuada5((12)))


def preco6(produtos):
  if len (produtos) == 0 :
    return produtos
  melhoropcao = produtos[0]
  menorpreco = melhoropcao[0] / melhoropcao[1]
  for produto in produtos[1:]:
    valor, peso = produto
    precograma = valor / peso
    if precograma < menorpreco:
      melhoropcao = produto
      menorpreco = precograma
  return melhoropcao
#print(preco6([]))
#print(preco6([[12,0.01]]))
#print(preco6([[10.5,800],[5,300.8],[2,150],[1,60]]))
#print(preco6([[12,800],[4,300],[3.5,150]]))
#print(preco6([[10,800],[5,300],[2,150],[1,60],[20,1800]]))


def passeiospossiveis7(conexoes, passeios):
    saida = 0
    for passeio in passeios:
        passeiovalido = 1
        anterior = 0
        for sala in passeio:
            if anterior != 0:
                conexao_valida = False
                for conexao in conexoes:
                    if (conexao == [anterior, sala]) or (conexao == [sala, anterior]):
                        conexao_valida = True
                        break  
                if not conexao_valida:
                    passeiovalido = 0
                    break  
            anterior = sala
        if passeiovalido == 1:
            saida += 1
    return saida

#print(passeiospossiveis7([[2, 3], [3, 4], [4, 2], [3, 5], [1, 5], [1, 2]],[[5, 3, 4, 3, 2], [1, 2, 3, 5, 4, 2], [4, 3, 5, 1, 2, 4], [1, 5, 3, 2, 4, 3, 4, 2, 1, 5, 1]])) 
#print(passeiospossiveis7([[1, 2], [3, 4]],[[1, 2, 1, 2], [4, 3, 4, 3, 4], [1, 4]])) 
#print(passeiospossiveis7([[1, 2], [1, 4], [1, 3], [2, 3], [3, 4]],[[1, 3, 2, 4, 1, 4], [1, 3, 2, 1, 4]]))