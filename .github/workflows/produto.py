def produto (lista):
  n = 1
  for numero in lista:
    if (type(numero) == int) or (type(numero) == float):
      n *= numero
  return n
print (produto([4,2,3]))
print (produto([4,2,3,1,2,0]))
print (produto([1.5,2,1j,2,3.5,'100']))
print (produto([True,1.1,2,1j,2.2,3.2]))