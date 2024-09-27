def caixadagua (caixat,bombat):
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
print (caixadagua (2,1))
print (caixadagua (2,0.5))
print (caixadagua (3,2))
print (caixadagua (20,15))
print (caixadagua (100,10))