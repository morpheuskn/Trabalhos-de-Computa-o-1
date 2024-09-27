def posicao (lista,numero):
  posicaol = []
  tamanho = 0
  while tamanho < len (lista):
    if lista[tamanho] == numero:
      posicaol.append(tamanho)
    tamanho += 1
  return posicaol
print (posicao([1,2,3,4,5,6,7,8,9],5))
print (posicao([1,2,2,1,3,4,1],1))
print (posicao([1,2,2,1,1],2))
print (posicao([2,2,2,2,2],2))
print (posicao([1,1,1],2))
print (posicao([],2))