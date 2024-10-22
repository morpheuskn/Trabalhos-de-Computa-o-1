def cr5 (notas, creditos):
  soma = 0
  creditostotais = 0
  for materia, nota in notas.items():
    soma += nota * creditos[materia]
    creditostotais += creditos[materia]
  media = soma / creditostotais
  return media
print(cr5({'Calculo I': 8.0,'Computacao I': 9.5, 'Quimica': 4}, {'Quimica': 2,'Calculo I': 5,'Computacao I': 4, 'Fisica Experimental': 3}))
print(cr5({'Calculo I': 8.0,'Computacao I': 9.5, 'Quimica': 4,'Fisica I': 5.1}, {'Fisica I': 5,'Quimica': 2,'Calculo I': 5,'Computacao I': 4, 'Fisica Experimental': 3}))
print(cr5({'Quimica': 9.5,'Fis Exp II': 10,'Calculo II': 7.1,'Computacao II': 5.5,'Fisica II': 0}, {'Calculo I': 5, 'Fisica II': 4,'Fisica I': 4,'Quimica': 2,'Calculo II': 5,'Computacao II': 6, 'Fis Exp II': 1}))    