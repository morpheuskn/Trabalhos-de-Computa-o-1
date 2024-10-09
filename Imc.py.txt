nome=str(input("Digite o seu nome: "))
idade=int(input("Digite a sua Idade: "))
altura=float(input("Digite a sua Altura: "))
peso=float(input("Digite o seu Peso: "))

def imc (altura,peso):
    resultado=peso/(altura**2)
    return resultado

IMC=imc(altura,peso)

def relatorio(nome,idade,altura,peso):
    
print("Nome: %s" %nome)
print("Idade: %.d" %idade)
print("Altura: %.2f" %altura)
print("Peso: %.2f" %peso)
print("IMC: %4.1f" %IMC)
