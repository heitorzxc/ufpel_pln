import string
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
def PreProcessamentoTextual(textoPreProcessado):
  # Remove caracteres especiais e pontuações
  textoPreProcessado = textoPreProcessado.translate(str.maketrans('', '', string.punctuation))
  # Converta tudo para minúsculas
  textoPreProcessado = textoPreProcessado.lower()
  # Retorne o texto pré-processado
  return textoPreProcessado
def AnalisadorDeFrequenciaTextual(textoDeEntrada):
  # Pré-processamento do texto
  textoPreProcessado = PreProcessamentoTextual(textoDeEntrada)
  # Tokenização do texto
  tokens = word_tokenize(textoPreProcessado)
  # Contagem de tokens
  contadorDeTokens = len(tokens)
  # Contagem de tipos
  contadorDeTipos = len(set(tokens))  # usando set para remover duplicatas
  # Frequência de tokens usando Counter
  contadorFrequencia = Counter(tokens)
  return contadorFrequencia, contadorDeTipos
def main():
  # Captura o texto que deseja analisar
  textoDeEntrada = input("Digite o texto que deseja analisar: ")
  # Analisa a frequência do texto
  frequenciaDeTokens, contadorDeTipos = AnalisadorDeFrequenciaTextual(textoDeEntrada)
  # Resultados
  print("Frequência dos tokens:")
  for token, frequency in frequenciaDeTokens.items():
      print(f"{token}: {frequency}")
  print("\nNúmero total de tipos:", contadorDeTipos)
if __name__ == "__main__":
  main()