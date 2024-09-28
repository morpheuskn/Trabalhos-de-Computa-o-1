def meio (lista,n1,n2):
  quanto = 0
  for n in lista:
    if (n <= n1 and n >= n2) or (n <= n2 and n >= n1):
     quanto += 1
  return (quanto)
print (meio([-1,0,1,1.2,3,4.5,4.9,5.1,6,7,8],1,5))
print (meio([1,7,1.2,3,8,6,4.9,5.1,4.5],10,50))
print (meio([0,0,0,0,0,0,0,0],0,0))
print (meio([-1,0.1,-1.2,4,10,2],-2,10))