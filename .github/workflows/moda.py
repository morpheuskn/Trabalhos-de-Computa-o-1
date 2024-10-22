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
#print(encontrar2([1, 2, 3, 3, 2, 1]))Deve retornar ['E23', 'O84']
print(encontrar([1, 2, 3, 3, 2, 1]))  # Deve retornar [1, 2, 3]