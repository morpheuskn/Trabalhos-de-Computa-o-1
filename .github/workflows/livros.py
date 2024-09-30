def livros (tupla1,tupla2,tupla3,tupla4):
  resultado = (tupla1 + tupla2 + tupla3 + tupla4)
  return resultado
print (livros( ('Mistborn',), ('Brandon Sanderson',), (766,), (2006,) ))
print (livros ( ('Mistborn', 'Percy Jackson'), ('Brandon Sanderson', 'Rick Riordan'), (766, 377), 
(2006, 2005)))
print (livros ( ('Mistborn', 'Percy Jackson', 'A Arma Escarlate'), ('Brandon Sanderson', 'Rick Riordan', 'Renata Ventura'), (766, 377, 667), (2006, 2005, 2012)))