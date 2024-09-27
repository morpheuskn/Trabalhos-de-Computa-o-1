def campominado(listajogador, listaminado):
    i = 0
    resposta = []
    while i < len(listajogador):
        xj = listajogador[i]
        yj = listajogador[i+1]
        j = 0
        colisao = 0
        while j < len(listaminado) and colisao == 0:
            xm = listaminado[j]
            ym = listaminado[j+1]
            if xj == xm and yj == ym:
                colisao = 1
            j += 2
        resposta.append(colisao)
        i += 2
    return resposta

print(campominado([0, 6, 3, 5], [10, 2, 0, 6, 3, 4, 9, 5]))
print(campominado([0, 6, 3, 5], [10, 3, 5, 6, 3, 4, 9, 5]))
print(campominado([0, 6, 3, 5, 10, 3, 9, 5], [10, 3, 5, 6, 3, 4, 9, 5]))
print(campominado([1, 1, 0, 7, 9, 5, 3, 5, 10, 3], [1, 1, 10, 3, 3, 4, 0, 7, 3, 1, 1, 10, 3, 4, 0, 7])),1,10,3,4,0,7]))