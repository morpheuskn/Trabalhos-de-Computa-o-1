def envio (dias,chips,chipac):
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
print(envio (1,5,5))
print(envio (10,25,5))
print(envio (10,26,5))
print(envio (2,12,10))
print(envio (3,14,10))