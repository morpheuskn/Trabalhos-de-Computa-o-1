def somaperiodo (n):
  soma = 0
  a = 1
  if n > 1:
    while n >= a:
      b = 0
      c = 1
      #print("b:",b,"c:",c)
      while a >= c:
        b += c
        c += 1
        #print("b1:",b,"c1:",c)
      soma += b
      a += 1
      #print("soma:",soma,"a:",a)
  return soma
print (somaperiodo (2))
print (somaperiodo (4))
print (somaperiodo (5))
print (somaperiodo (10))
print (somaperiodo (500))