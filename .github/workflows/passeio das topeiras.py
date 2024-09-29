def passeiospossiveis(conexoes, passeios):
  contador = 0
  for i in range(len(passeios)-1):
    for passeio in passeios:
      if [passeio[i], passeio[i + 1]] not in conexoes and [passeio[i + 1], passeio[i]] not in conexoes:
        contador += 0
      else:
        contador += 1 
    return contador


print(passeiospossiveis([[2, 3], [3, 4], [4, 2], [3, 5], [1, 5], [1, 2]], [[5, 3, 4, 3, 2], [1, 2, 3, 5, 4, 2], [4, 3, 5, 1,2, 4], [1, 5, 3, 2, 4, 3, 4, 2, 1, 5, 1]]))#deve retorna 3
print(passeiospossiveis([[1, 2], [3, 4]], [[1, 2, 1, 2], [4, 3, 4, 3, 4], [1, 4]]))#deve retornar 2
print(passeiospossiveis([[1, 2], [1, 4], [1, 3], [2, 3], [3, 4]], [[1, 3, 2, 4, 1, 4], [1, 3, 2, 1, 4]]))#deve retorna 1