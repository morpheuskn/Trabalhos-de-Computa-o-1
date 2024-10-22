import random
def geragabarito3(questoes, respostas):
    gabarito = {}
    for i in range(1, questoes + 1):
        gabarito[i] = random.choice(respostas)
    return gabarito
random.seed(0) 
print(geragabarito3(5, ['a', 'b', 'c']))
print(geragabarito3(5, ['a', 'b', 'c', 'd']))
print(geragabarito3(10, ['a', 'b', 'c', 'd', 'e']))
print(geragabarito3(15, ['a', 'b', 'c']))c']))dutibilidade do exemplo
print(gerar_gabarito(5, ['a', 'b', 'c']))
