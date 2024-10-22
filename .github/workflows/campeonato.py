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

print(campeonato6((('PAL', 'SAN', 'FLA', 'CAM'),('COR', 'PAL', 'SAN', 'GRE'),('PAL', 'FLA', 'INT', 'GRE'),('FLA', 'SAN', 'PAL', 'GRE'),('FLA', 'INT', 'CAM', 'SAO'),('CAM', 'FLA', 'PAL', 'FOR'))))
print(campeonato6((('Bucks', 'Raptors', '76ers', 'Celtics'),('Bucks', 'Raptors', 'Celtics', 'Pacers'),('76ers', 'Nets', 'Bucks', 'Knicks'),('Heat', 'Celtics', 'Bucks', '76ers'))))
print(campeonato6((('Warriors', 'Nuggets', 'Trail Blazers', 'Rockets'),('Lakers', 'Clippers', 'Nuggets', 'Rockets'),('Jazz', 'Suns', 'Nuggets', 'Clippers'),('Suns', 'Grizzlies', 'Warriors', 'Mavericks'))))))avericks')) ) )