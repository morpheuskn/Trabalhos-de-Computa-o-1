def primo4a (numero):
  a = 2
  if 2 > numero:
    return False
  while a * a <= numero:
    if numero % a == 0:
      return False
    a += 1
  return True
print (primo4a (1))
print (primo4a (2))
print (primo4a (7))
print (primo4a (9))
print (primo4a (11))



def primo4b (numero):
  if primo4a (numero) == True:
    return numero
  else:
    while primo4a (numero) == False:
      numero += 1
    return numero
    
print (primo4b (3))
print (primo4b (9))
print (primo4b (12))
print (primo4b (32))
print (primo4b (55))   primo4b (32))
print (primo4b (55))
    