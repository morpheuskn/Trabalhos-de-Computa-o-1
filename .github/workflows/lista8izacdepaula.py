import random

def romano1 (n):
  dicionario = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X"}
  if n not in dicionario:
    return '""'
  else:
    return dicionario[n]
#print (romano1 (1))
#print (romano1 (2))
#print (romano1 (3))
#print (romano1 (4))
#print (romano1 (5))
#print (romano1 (6))
#print (romano1 (7))
#print (romano1 (8))
#print (romano1 (9))
#print (romano1 (10))
#print (romano1 (11))
#print (romano1 (12))
#print (romano1 (13))


def encontrar2(lista):
    frequencias = {}
    for valor in lista:
        if valor in frequencias:
            frequencias[valor] += 1
        else:
            frequencias[valor] = 1
    maior_frequencia = 0
    for valor in frequencias:
        if frequencias[valor] > maior_frequencia:
            maior_frequencia = frequencias[valor]
    modas = []
    for valor in frequencias:
        if frequencias[valor] == maior_frequencia:
            modas.append(valor)
    
    return modas
#print(encontrar2([1, 1, 2, 3, 4, 1, 4]))  
#print(encontrar2([2.3, 5.1, 7.6, -2.3, 3.9, 5.1]))
#print(encontrar2(['H01', 'E23', 'A59', 'B72', 'E23', 'O84', 'O84', 'C21']))
#print(encontrar2([1, 2, 3, 3, 2, 1]))


def geragabarito3(questoes, respostas):
    gabarito = {}
    for i in range(1, questoes + 1):
        gabarito[i] = random.choice(respostas)
    return gabarito
#random.seed(0) 
#print(geragabarito3(5, ['a', 'b', 'c']))
#print(geragabarito3(5, ['a', 'b', 'c', 'd']))
#print(geragabarito3(10, ['a', 'b', 'c', 'd', 'e']))
#print(geragabarito3(15, ['a', 'b', 'c']))


def dano4(danomin, danomax, chancecritica, armadura): 
    danobase = random.randint(danomin, danomax)
    dado = random.randint(0, 100)
    
    if dado <= chancecritica:
        danototal = danobase * 2
        
    else:
        danototal = danobase
        
    if danototal > armadura:
        return danototal - armadura
        
    else:
        return 0

def batalha4(player1, player2):
    vidaplayer1, danominplayer1, danomaxplayer1, armaduraplayer1, chancecriticaplayer1 = player1
    vidaplayer2, danominplayer2, danomaxplayer2, armaduraplayer2, chancecriticaplayer2 = player2
    turnos = 0
    
    while vidaplayer1 > 0 and vidaplayer2 > 0:
        turnos += 1 
        
        if vidaplayer1 > 0:
            danocausado = dano4(danominplayer1, danomaxplayer1, chancecriticaplayer1, armaduraplayer2)
            vidaplayer2 -= danocausado
            if vidaplayer2 <= 0:
                return (1, vidaplayer1, turnos)  # Player 1 venceu
        
        if vidaplayer2 > 0:
            danocausado = dano4(danominplayer2, danomaxplayer2, chancecriticaplayer2, armaduraplayer1)
            vidaplayer1 -= danocausado
            if vidaplayer1 <= 0:
                return (2, vidaplayer2, turnos)  # Player 2 venceu
#random.seed(0)
#print(batalha4((10, 5, 6, 8, 0), (5, 1, 2, 0, 5)))
#print(batalha4((30, 8, 10, 8, 60), (10, 2, 4, 0, 20)))
#print(batalha4((6, 9, 12, 0, 5), (15, 3, 4, 15, 95)))
#print(batalha4((20, 3, 10, 0, 10), (20, 1, 3, 5, 40)))
#print(batalha4((20, 7, 15, 5, 10), (10, 3, 8, 5, 30)))
#print(batalha4((40, 10, 15, 10, 60), (100, 20, 30, 0, 0)))


def cr5 (notas, creditos):
  soma = 0
  creditostotais = 0
  for materia, nota in notas.items():
    soma += nota * creditos[materia]
    creditostotais += creditos[materia]
  media = soma / creditostotais
  return media
#print(cr5({'Calculo I': 8.0,'Computacao I': 9.5, 'Quimica': 4}, {'Quimica': 2,'Calculo I': 5,'Computacao I': 4, 'Fisica Experimental': 3}))
#print(cr5({'Calculo I': 8.0,'Computacao I': 9.5, 'Quimica': 4,'Fisica I': 5.1}, {'Fisica I': 5,'Quimica': 2,'Calculo I': 5,'Computacao I': 4, 'Fisica Experimental': 3}))
#print(cr5({'Quimica': 9.5,'Fis Exp II': 10,'Calculo II': 7.1,'Computacao II': 5.5,'Fisica II': 0}, {'Calculo I': 5, 'Fisica II': 4,'Fisica I': 4,'Quimica': 2,'Calculo II': 5,'Computacao II': 6, 'Fis Exp II': 1}))


def campeonato6(tupla):
    resultados = {}
    index = 0 

    for temporada in tupla:
        posicao = 1 
        for time in temporada:
            if time not in resultados:
                resultados[time] = ['-'] * len(tupla) 
            resultados[time][index] = posicao  
            posicao += 1  
        index += 1  

    return resultados

#print(campeonato6((('PAL', 'SAN', 'FLA', 'CAM'),('COR', 'PAL', 'SAN', 'GRE'),('PAL', 'FLA', 'INT', 'GRE'),('FLA', 'SAN', 'PAL', 'GRE'),('FLA', 'INT', 'CAM', 'SAO'),('CAM', 'FLA', 'PAL', 'FOR'))))
#print(campeonato6((('Bucks', 'Raptors', '76ers', 'Celtics'),('Bucks', 'Raptors', 'Celtics', 'Pacers'),('76ers', 'Nets', 'Bucks', 'Knicks'),('Heat', 'Celtics', 'Bucks', '76ers'))))
#print(campeonato6((('Warriors', 'Nuggets', 'Trail Blazers', 'Rockets'),('Lakers', 'Clippers', 'Nuggets', 'Rockets'),('Jazz', 'Suns', 'Nuggets', 'Clippers'),('Suns', 'Grizzlies', 'Warriors', 'Mavericks'))))    