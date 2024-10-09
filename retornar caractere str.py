x=str(input())
y=str(input())

def cars(x,y):
    if x=="":
        return False
    if x[0]==y:
        return True
    return cars(x[1:],y)
        
   
print(cars(x,y))
