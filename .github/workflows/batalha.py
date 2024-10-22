import random

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
random.seed(0)
print(batalha4((10, 5, 6, 8, 0), (5, 1, 2, 0, 5)))
print(batalha4((30, 8, 10, 8, 60), (10, 2, 4, 0, 20)))
print(batalha4((6, 9, 12, 0, 5), (15, 3, 4, 15, 95)))
print(batalha4((20, 3, 10, 0, 10), (20, 1, 3, 5, 40)))
print(batalha4((20, 7, 15, 5, 10), (10, 3, 8, 5, 30)))
print(batalha4((40, 10, 15, 10, 60), (100, 20, 30, 0, 0))), 30)
personagem2 = (90, 8, 25, 8, 20)

resultado = batalha_rpg(personagem1, personagem2)
print(f"Vencedor: Personagem {resultado[0]}, Vida restante: {resultado[1]}, Turnos: {resultado[2]}")
