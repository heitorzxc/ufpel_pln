# Peça ao usuário para inserir uma frase ou uma palavra. Em seguida, crie um programa que conte quantas vogais e consoantes estão presentes na entrada. Exiba os resultados.
import string
# Conjuntos de vogais e consoantes com letras minúsculas e acentuadas
minusculasVogais = {'a', 'á', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'õ', 'u', 'ú', 'ü'}
minusculasConsoantes = {'b', 'c', 'ç', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
# Conjuntos de vogais e consoantes com letras maiúsculas e acentuadas
maiusculasVogais = {'A', 'Á', 'Â', 'Ã', 'E', 'É', 'Ê', 'I', 'Í', 'O', 'Ó', 'Ô', 'Õ', 'U', 'Ú', 'Ü'}
maiusculasConsoantes = {'B', 'C', 'Ç', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'}
# Achei interessante gerar os caracteres separadamente e depois unir em dois grupos
vogais = minusculasVogais.union(maiusculasVogais)
consoantes = minusculasConsoantes.union(maiusculasConsoantes)
frase = input("Digite uma frase ou palavra: ")
# Usando o método split para dividir a frase em uma lista de palavras
lista = frase.split()
# Contadores inicializados para poder incrementar depois
numVogais = 0
numConsoantes = 0
# Loop de palavra em palavra
for palavra in lista:
  for letra in palavra:
    if letra in vogais:
      # vogais
      numVogais += 1
    elif letra in consoantes:
      # consoantes
      numConsoantes += 1
    else:
      # caractere de espaço em branco ou outros caracteres não considerados
      continue
print("Número de vogais:", numVogais)
print("Número de consoantes:", numConsoantes)