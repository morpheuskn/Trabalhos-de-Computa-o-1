def cacatesouro (jogadorx,jogadory,jogox,jogoy):
  x = 0
  y = 0
  if type(jogox) != int or type(jogoy) != int:
    return (-3,-3)
  if jogox < 0 or jogox > 9 or jogoy < 0 or jogoy > 9:
    return (-2,-2)
  if jogadorx == jogox:
    x = 0
  if jogadorx > jogox:
    x = -1
  if jogadorx < jogox:
    x = 1
  if jogadorx < 0 or jogadorx > 9:
    x = -2
  if not (type(jogadorx) == int):
    x = -3
  if jogadory == jogoy:
    y = 0
  if jogadory > jogoy:
    y = -1
  if jogadory < jogoy:
    y = 1
  if jogadory < 0 or jogadory > 9:
    y = -2
  if not (type(jogadory) == int):
    y = -3
  return (x,y)
print (cacatesouro(9,1,7,6))
print (cacatesouro(6,4,7,6))
print (cacatesouro(7,8,7,6))
print (cacatesouro(5,11,7,6))
print (cacatesouro(9,2.5,7,6))
print (cacatesouro(12,2.5,7,6))
print (cacatesouro(1,11.1,7,6))
print (cacatesouro(1,2,10,6))
print (cacatesouro(1,2,5.0,6))
print (cacatesouro(1,2,4, 12.4))