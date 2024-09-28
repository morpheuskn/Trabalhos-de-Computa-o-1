def preco(produtos):
  if len (produtos) == 0 :
    return produtos
  melhoropcao = produtos[0]
  menorpreco = melhoropcao[0] / melhoropcao[1]
  for produto in produtos[1:]:
    valor, peso = produto
    precograma = valor / peso
    if precograma < menorpreco:
      melhoropcao = produto
      menorpreco = precograma
  return melhoropcao
print(preco([]))
print(preco([[12,0.01]]))
print(preco([[10.5,800],[5,300.8],[2,150],[1,60]]))
print(preco([[12,800],[4,300],[3.5,150]]))
print(preco([[10,800],[5,300],[2,150],[1,60],[20,1800]]))o([[10,800],[5,300],[2,150],[1,60],[20,1800]]))