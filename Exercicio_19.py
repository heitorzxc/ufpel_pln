from math import log2

# Calcula a entropia de um conjunto de palavras
def calcular_entropia(palavra):
  proporcoes = {}
  total_letras = len(palavra)

  for letra in palavra:
    if letra in proporcoes:
      proporcoes[letra] += 1
    else:
      proporcoes[letra] = 1

  entropia = 0
  for letra, ocorrencias in proporcoes.items():
    proporcao = ocorrencias / total_letras
    entropia -= proporcao * log2(proporcao)

  return entropia

# Conjuno de palavras a serem analisadas
palavras = ["ARARAQUARA", "UFPEL", "PELOTAS", "LUCIANA", "SIMONE"]

# Calcula a entropia de cada palavra e imprime o resultado
for palavra in palavras:
  entropia = calcular_entropia(palavra)
  print(f"A entropia de '{palavra}' é: {entropia}")

# A palavra mais complexa é 'SIMONE', pois possui a maior entropia. Isso significa que a palavra 'SIMONE' possui a maior quantidade de letras diferentes em relação ao total de letras.