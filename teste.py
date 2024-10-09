def converte (h,m):
    return h*60+m
    
h1=int(input())
m1=int(input())
h2=int(input())
m2=int(input())


def calcula_diferenca(h1,m1,h2,m2):
    q1=converte(h1,m1)
    q2=converte(h2,m2)
    return q2-q1

resp=calcula_diferenca(h1,m1,h2,m2)

print("Quantidade de Minutos Trabalhados: %d" %resp)
    
