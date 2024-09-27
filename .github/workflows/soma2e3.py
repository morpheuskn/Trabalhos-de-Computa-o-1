def soma2e3 (a,b):
  soma = 0
  if a < b:
    while a <= b:
      if ((a % 2 != 0) or (a % 3 != 0)) and ((a % 2 == 0) or (a % 3 == 0)):
        soma += a
      a = a+1
  elif b < a:
    while b <= a:
      if ((b % 2 != 0) or (b % 3 != 0)) and ((b % 2 == 0) or (b % 3 == 0)):
        soma += b
      b = b+1
  return soma
print (soma2e3 (1,3))
print (soma2e3 (1,10))
print (soma2e3 (1,12))
print (soma2e3 (10,5))