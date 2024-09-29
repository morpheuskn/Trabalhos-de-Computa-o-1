def passeiospossiveis(conexoes, passeios):
    saida = 0
    for passeio in passeios:
        passeiovalido = 1
        anterior = 0
        for sala in passeio:
            if anterior != 0:  
                if [anterior, sala] not in conexoes and [sala, anterior] not in conexoes:
                    passeiovalido = 0
            anterior = sala
        if passeiovalido == 1:
            saida += 1
    return saida
print(passeiospossiveis([[2, 3], [3, 4], [4, 2], [3, 5], [1, 5], [1, 2]], [[5, 3, 4, 3, 2], [1, 2, 3, 5, 4, 2], [4, 3, 5, 1, 2, 4], [1, 5, 3, 2, 4, 3, 4, 2, 1, 5, 1]])) 
print(passeiospossiveis([[1, 2], [3, 4]], [[1, 2, 1, 2], [4, 3, 4, 3, 4], [1, 4]])) 
print(passeiospossiveis([[1, 2], [1, 4], [1, 3], [2, 3], [3, 4]], [[1, 3, 2, 4, 1, 4], [1, 3, 2, 1, 4]])) 