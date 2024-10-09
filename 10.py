ano=int(input("Digite o Ano: "))

def descobre_X(ano):
    if ano < 1900 or ano > 2299:
        print("Impossível de Calcular")
        return
    if ano >=1900 or ano <=2199:
         24
         return 24
    if ano >=2200 or ano <=2299:
        25
        return 25
    return

def descobre_Y(ano):
    if ano < 1900 or ano > 2299:
        print("Impossível de Calcular")
        return
    if ano >=1900 or ano <=2099:
         5
         return 5
    if ano >=2100 or ano <=2199:
        6
        return 6
    if ano >=2200 or ano <=2299:
        7
        return 7
    return

X=(descobre_X(ano))

Y=(descobre_Y(ano))

A=ano%19
B=ano%4
C=ano%7
D=(19*A+X)%30
E=(2*B+4*C+6*D+Y)%7


def exibe_dia_mes(A,D,E):
    if D+E>9:
        Dia=D+E-9
        Mes=4
        
        if Dia==26:
            Dia=19
            
        else:
            if Dia==25 and D==28 and A>10:
                Dia=18
    else:
        Dia = D+E+22
        Mes = 3
    print("Dia: %d\tMês: %d" %(Dia,Mes))
    return



print(exibe_dia_mes(A,D,E))


