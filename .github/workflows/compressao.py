def compressao (lista):    
  saida = []
  repeticao = 0
  vezes = 0
  while repeticao < len(lista):
    vezes = 1
    while repeticao + 1 < len(lista) and lista[repeticao] == lista[repeticao + 1]:
      vezes += 1
      repeticao += 1
    saida.append(vezes)
    saida.append(lista[repeticao])
    repeticao += 1
  return saida
print(compressao([1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4]))
print(compressao([0,0,0,0,1,1,1,1,0,0,0,0]))
print(compressao([2,2,2,2,2,1,1,1,0,0,0,0,0,1,1,1,3,3,3]))
print(compressao([0,0,0,0,0,0,1,1,3,3,4,1,1,4,4,4,4]))4]))ssão RLE:

def rle_compress(lst):
    # Verifica se a lista está vazia
    if not lst:
        return []

    compressed = []
    i = 0

    # Percorre a lista usando while
    while i < len(lst):
        count = 1
        # Conta quantos elementos consecutivos são iguais
        while i + 1 < len(lst) and lst[i] == lst[i + 1]:
            count += 1
            i += 1
        # Adiciona o número de repetições seguido do valor
        compressed.append(count)
        compressed.append(lst[i])
        i += 1
    
    return compressed

# Teste com os exemplos dados
test_1 = [1, 1, 1, 1, 2, 1, 1, 1]
test_2 = [1, 2, 3, 4, 1]

print(rle_compress(test_1))  # Saída: [4, 1, 1, 2, 3, 1]
print(rle_compress(test_2))  # Saída: [1, 1, 1, 2, 1, 3, 1, 4, 1, 1]

'''Explicação do código:

1. A função rle_compress recebe uma lista de números como argumento.


2. A função inicia com uma verificação para garantir que a lista não está vazia.


3. Utilizamos um loop while para percorrer a lista. Quando encontramos números consecutivos iguais, o programa conta quantos são.


4. Após contar os valores consecutivos, adicionamos o número de repetições seguido pelo valor correspondente na lista comprimida.


5. Continuamos esse processo até o final da lista.


6. O resultado final é uma lista comprimida conforme a técnica RLE.'''



'''Testes:

Para a entrada [1, 1, 1, 1, 2, 1, 1, 1], a saída será [4, 1, 1, 2, 3, 1].

Para a entrada [1, 2, 3, 4, 1], a saída será [1, 1, 1, 2, 1, 3, 1, 4, 1, 1].'''


�da será [1, 1, 1, 2, 1, 3, 1, 4, 1, 1].'''


