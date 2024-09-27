def euclides (lista1,lista2):
  n = 0
  soma = 0
  d1 = len(lista1)
  d2 = len(lista2)
  resposta = []
  while n < d1 and n < d2:
    a = (lista1[n] - lista2[n])**2
    n += 1
    soma += a
  soma = soma**(1/2)
  resposta.append(soma)
  return resposta
print (euclides ([1,2],[1,2]))
print (euclides ([0,0],[3,4]))
print (euclides ([3,4],[0,0]))
print (euclides ([1.5,10,1],[5,4,1]))
print (euclides ([1,2,3,4,5],[6,7,8,9,10]))