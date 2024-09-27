def posicao1 (lista,numero):
  posicaol = []
  tamanho = 0
  while tamanho < len (lista):
    if lista[tamanho] == numero:
      posicaol.append(tamanho)
    tamanho += 1
  return posicaol
#print (posicao1 ([1,2,3,4,5,6,7,8,9],5))
#print (posicao1 ([1,2,2,1,3,4,1],1))
#print (posicao1 ([1,2,2,1,1],2))
#print (posicao1 ([2,2,2,2,2],2))
#print (posicao1 ([1,1,1],2))
#print (posicao1 ([],2))


def euclides2 (lista1,lista2):
  n = 0
  soma = 0
  d1 = len(lista1)
  d2 = len(lista2)
  resposta = []
  while n < d1 and n < d2:
    a = (lista1[n] - lista2[n])**2
    n += 1
    soma += a
  soma = soma**(1/2)
  resposta.append(soma)
  return resposta
#print (euclides2 ([1,2],[1,2]))
#print (euclides2 ([0,0],[3,4]))
#print (euclides2 ([3,4],[0,0]))
#print (euclides2 ([1.5,10,1],[5,4,1]))
#print (euclides2 ([1,2,3,4,5],[6,7,8,9,10]))


def compressao3 (lista):    
  saida = []
  repeticao = 0
  vezes = 0
  while repeticao < len(lista):
    vezes = 1
    while repeticao + 1 < len(lista) and lista[repeticao] == lista[repeticao + 1]:
      vezes += 1
      repeticao += 1
    saida.append(vezes)
    saida.append(lista[repeticao])
    repeticao += 1
  return saida
#print(compressao3 ([1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4]))
#print(compressao3 ([0,0,0,0,1,1,1,1,0,0,0,0]))
#print(compressao3 ([2,2,2,2,2,1,1,1,0,0,0,0,0,1,1,1,3,3,3]))
#print(compressao3 ([0,0,0,0,0,0,1,1,3,3,4,1,1,4,4,4,4]))


def envio4 (dias,chips,chipac):
  pacotes = 0
  resto = 0
  chipspdia = [chips] * dias
  pacotespdia = []
  vezes = 0
  producaopdia = 0
  pacotenviados = 0
  while vezes < dias:
    producaopdia = chipspdia [vezes] + resto
    pacotenviados = producaopdia // chipac
    pacotespdia.append (pacotenviados)
    pacotes += pacotenviados
    resto = producaopdia % chipac
    vezes += 1
  return pacotes
#print(envio4 (1,5,5))
#print(envio4 (10,25,5))
#print(envio4 (10,26,5))
#print(envio4 (2,12,10))
#print(envio4 (3,14,10))