def valor (n):
  if n == 0:
    return 0
  else:
    saida = 0
    for i in range (1, n+1):
      saida += 1/(i * 2)
    return saida
print (valor(0))
print (valor(1))
print (valor(2))
print (valor(4))