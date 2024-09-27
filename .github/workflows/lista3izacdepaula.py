def soma1 (a,b):
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
#print (soma1 (1,3))
#print (soma1 (1,10))
#print (soma1 (1,12))
#print (soma1 (10,5))


def somaperiodo2 (n):
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
#print (somaperiodo2 (2))
#print (somaperiodo2 (4))
#print (somaperiodo2 (5))
#print (somaperiodo2 (10))
#print (somaperiodo2 (500))


def transmissao3 (dia0,fatort,diast):
  dia = 1 
  infectados = dia0
  infectadost = dia0
  while dia <= diast:
    infectados *= fatort
    infectadost += infectados
    dia += 1
  return infectadost
#print (transmissao3 (1,5,3))
#print (transmissao3 (2,1,5))
#print (transmissao3 (2,4,10))


def primo4a (numero):
  a = 2
  if 2 > numero:
    return False
  while a * a <= numero:
    if numero % a == 0:
      return False
    a += 1
  return True
#print (primo4a (1))
#print (primo4a (2))
#print (primo4a (7))
#print (primo4a (9))
#print (primo4a (11))



def primo4b (numero):
  if primo4a (numero) == True:
    return numero
  else:
    while primo4a (numero) == False:
      numero += 1
    return numero
    
#print (primo4b (3))
#print (primo4b (9))
#print (primo4b (12))
#print (primo4b (32))
#print (primo4b (55))


def caixadagua5 (caixat,bombat):
  caixag = 0
  bomba = bombat
  dia = 0
  caixa = 0
  while caixag < caixat:
    caixag = (caixa + bomba)/2
    caixa = caixag
    bomba += bomba * 0.2
    dia += 1
  return (dia)
#print (caixadagua5 (2,1))
#print (caixadagua5 (2,0.5))
#print (caixadagua5 (3,2))
#print (caixadagua5 (20,15))
#print (caixadagua5 (100,10))