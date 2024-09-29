def contar_passeios_possiveis(conexoes, passeios):
    
    def passeio_possivel(passeio):
        for i in range(len(passeio) - 1):
           
            if [passeio[i], passeio[i + 1]] not in conexoes and [passeio[i + 1], passeio[i]] not in conexoes:
                return False  
        return True  
    
    
    contador = 0
    for passeio in passeios:
        if passeio_possivel(passeio):
            contador += 1
    
    return contador


print(contar_passeios_possiveis([[2, 3], [3, 4], [4, 2], [3, 5], [1, 5], [1, 2]], [[5, 3, 4, 3, 2], [1, 2, 3, 5, 4, 2], [4, 3, 5, 1,2, 4], [1, 5, 3, 2, 4, 3, 4, 2, 1, 5, 1]]))
print(contar_passeios_possiveis([[1, 2], [3, 4]], [[1, 2, 1, 2], [4, 3, 4, 3, 4], [1, 4]]))
print(contar_passeios_possiveis([[1, 2], [1, 4], [1, 3], [2, 3], [3, 4]], [[1, 3, 2, 4, 1, 4], [1, 3, 2, 1, 4]]))