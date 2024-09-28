def comparacao (lista1,lista2):
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
print(comparacao([3,6,7,7,9],[4,6,4,8,5]))
print(comparacao([8,2,5,5,7,8],[7,2,7,4,9,10]))
print(comparacao([3,3,10,3,3,3,4],[2,1,7,10,4,1,8]))     ))     