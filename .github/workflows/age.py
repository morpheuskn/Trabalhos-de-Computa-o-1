i=int(input("Digite a sua Idade: "))
a=int(input("Digite o Ano: "))
c=("s")
if c=="s" or c=="S":
  def resposta():
    if i >= 100:
      print("Esse é o ano",a,"e você já chegou lá.")
    else:
      r=int(100)-i
      r2=a+r
      print("Faltam apenas",r,"anos para você ter 100 anos")
      print("Você chegará à",r,"anos, no ano de",r2,".")
 if c=="n" or c=="N":
   print("Programa Finalizado")
 resposta()
 c=str(input("Digite s ou S se quiser continuar, ou n ou N se quiser parar: "))
 