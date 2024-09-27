def calcgorjeta1 (a,b,c,d,e):
  g=(a+b+c+d+e)/10
  return (a+b+c+d+e+g)
 
#print (calcgorjeta1 (1,2,3,4,5))
#print (calcgorjeta1 (5,5,4,6,10))
#print (calcgorjeta1 (10,10,10,10,10))


def calcfuncao2(x):
  y=(x**(5/3))+(((x**2)-8*x)/10)-(((5*x**4)+(9*x**3)-(10*x**2))/((x**5)+2))**(1/2)
  return y
  
#print (calcfuncao2(0.8))
#print (calcfuncao2(1))
#print (calcfuncao2(2))
#print (calcfuncao2(10))


def Calcohn3 (r1,r2,If):
  Req=(r1*r2)/(r1+r2)
  V=Req*If
  i1=V/r1
  i2=V/r2
  return V,i1,i2
#print (Calcohn3 (3,4,2))
#print (Calcohn3 (8,2,10))
#print (Calcohn3 (20,20,200))
#print (Calcohn3 (0.5,99.5,20))


def calctemperatura4 (f):
  c=(f-32)/1.8000
  k=((f-32)/1.800)+273
  return (c,k)
#print (calctemperatura4 (0))
#print (calctemperatura4 (32))
#print (calctemperatura4 (100))
#print (calctemperatura4 (212))


def calccarro5 (s1,s2,vf,vi):
  ds=s2-s1
  a=((vi**2)-(vf**2))/(2*ds)
  return (a)
#print (calccarro5 (0,10,2,2))
#print (calccarro5 (5,10,10,20))
#print (calccarro5 (2,12,0,20))
#print (calccarro5 (10,110,2,4))


def calcarea6 (d,h):
  b=((d**2)-(h**2))**(1/2)
  a=(h*b)
  return (a)
#print (calcarea6 (5,4))
#print (calcarea6 (5,4))
#print (calcarea6 (50,10))


def calcexponencial7 (x):
  a=2*1
  b=3*2*1
  c=4*3*2*1
  d=5*4*3*2*1
  e=6*5*4*3*2*1
  f=7*6*5*4*3*2*1
  g=(((x**0)/1)+((x**1)/1)+((x**2)/a)+((x**3)/b)+((x**4)/c)+((x**5)/d)+((x**6)/e)+((x**7)/f))
  return (g)
#print (calcexponencial7 (0))
#print (calcexponencial7 (1))
#print (calcexponencial7 (2))
#print (calcexponencial7 (4))