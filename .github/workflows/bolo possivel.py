def bolototal (ot,on,ft,fn):
  
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
  
print (bolototal(6,6,200,200))
print (bolototal(18,6,600,200))
print (bolototal(18,6,500,200))
print (bolototal(4,5,150,100))
print (bolototal(8,3,100,300))
print (bolototal(2,18,100,250))
print (bolototal(2,18.2,100,250))
print (bolototal(2,18,100,-250))
print (bolototal(2,18,'100',250))
print (bolototal(5,0,300,150))100,250))
print (bolototal(2,18,100,-250))
print (bolototal(2,18,'100',250))
print (bolototal(5,0,300,150))