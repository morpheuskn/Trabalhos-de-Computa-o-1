def boolean1 (a):
  a1=type(a)
  if (a1 == int or a1 == float) and a > 0:
    return True
  else:
    return False
  return
#print (boolean1 (2))
#print (boolean1 (1.5))
#print (boolean1 (-4))
#print (boolean1 (0))
#print (boolean1 (-0.1))
#print (boolean1 ("16"))
#print (boolean1 (True))

def max2 (x):
  a = 0
  if x <= 1 and x >= -1:
    return (x)
  if x > 1 :
    a = 1
  if x < -1:
    a = -1
  return a
#print (max2 (0.5))
#print (max2 (-0.5))
#print (max2 (1))
#print (max2 (2))
#print (max2 (-5))

def jogobolas3 (be,bt,tl,tc):
    pe = (be / bt) * 100
    if be == bt:
        pb = 100
    elif pe > 70:
        pb = 50
    elif 30 <= pe <= 70:
        pb = 25
    else:
        pb = 0
    if tc <= tl:
        p = pb
    elif tc <= (tl + 10):
        p = (pb * 0.8)
    elif tc <= (tl + 30):
        p = (pb * 0.4)
    else:
        p = 0
    return(p)
#print (jogobolas3 (8,8,20,15))
#print (jogobolas3 (8,10,20,15))
#print (jogobolas3 (7,10,20,15))
#print (jogobolas3 (2,8,20,15))
#print (jogobolas3 (5,10,20,20))
#print (jogobolas3 (5,10,20,25))
#print (jogobolas3 (5,10,10,25))
#print (jogobolas3 (5,10,20,50))
#print (jogobolas3 (5,10,20,60))

def pontoreta4 (a,b,c):
  M = a
  m = a
  if b < m:
    m = b
  if b > M:
    M = b
  if c < m:
    m = c
  if c > M:
    M = c
  if (M - m) < 0:
    n = (M - m) * -1
  elif (M - m) > 0:
    n = M - m
  return n
  
#print(pontoreta4 (-1,-2,-3))
#print(pontoreta4 (5,10,1))
#print(pontoreta4 (2,-4,7))
#print(pontoreta4 (1,3,-1))
#print(pontoreta4 (9,9,15))

def gastoagua5 (a):
 
  if a <= 15:
    b = 10
    c = 0
    d = 0
    e = b + c + d
  if a >= 16 and a <= 40:
    b = 10
    c = (a - 15) * 1.2
    d = 0
    e = b + c + d
  if a >= 41:
    b = 10
    c = ((a - (a - 40)) - 15) * 1.2
    d = (a - 40) * 3.0
    e = b + c + d
    
  return (e,c,d)
  
#print(gastoagua5 (12))
#print(gastoagua5 (15))
#print(gastoagua5 (20))
#print(gastoagua5 (40))
#print(gastoagua5 (45))
#print(gastoagua5 (55))

def bolototal6 (ot,on,ft,fn):
  
  if not (type (ot) == int and type (on) == int and type (ft) == int and type (fn) == int):
    return (-1,-1,-1)
  
  if ot <= 0 or on <= 0 or ft <= 0 or fn <= 0:
    return (-1,-1,-1)
    
  bpo = ot // on
  bpf = ft // fn
  
  if bpo < bpf:
    bp = bpo
  else:
    bp = bpf
    
  os = ot - (bp * on)
  
  if os < on:
    ob = on - os
  else:
    ob = 0
    
  if ob > 0:
    co = (ob + 11) // 12
  else:
    co = 0
    
  fr = ft - (bp * fn)
  
  if fr < fn:
    fb = fn - fr
  else:
    fb = 0
    
  return (bp, co, fb)
  
#print (bolototal6 (6,6,200,200))
#print (bolototal6 (18,6,600,200))
#print (bolototal6 (18,6,500,200))
#print (bolototal6 (4,5,150,100))
#print (bolototal6 (8,3,100,300))
#print (bolototal6 (2,18,'100',250))
#print (bolototal6 (2,18.2,100,250))
#print (bolototal6 (2,18,100,-250))rint (bolototal6 (2,18,100,250))
#print (bolototal6 (2,18.2,100,250))
#print (bolototal6 (2,18,100,-250))(2,18,100,-250))