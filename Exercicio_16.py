import string
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
def PreProcessadorDeTexto(textoDeEntrada):
  # Remove caracteres especiais e pontuações que não são parte das palavras
  textoDeEntrada = textoDeEntrada.translate(str.maketrans('', '', string.punctuation))
  # Converte todas as palavras para letras minúsculas
  textoDeEntrada = textoDeEntrada.lower()
  # Retorna o texto pré-processado
  return textoDeEntrada
def AnalisadorDeFrequenciaTextual(textoEntrada):
  # Pré-processa o texto removendo caracteres especiais e pontuações
  textoPreProcessado = PreProcessadorDeTexto(textoEntrada)
  # Tokeniza as palavras
  tokens = word_tokenize(textoPreProcessado)
  # Conta o número de tokens
  contadorTokens = len(tokens)
  # Conta o número de tipos
  contadorTipos = len(set(tokens))  # usando set para remover duplicatas
  # Conta a frequência dos tokens
  contadorFrequencia = Counter(tokens)
  # Retorna o número total de tokens, o número total de tipos e a frequência dos tokens
  return contadorTokens, contadorTipos, contadorFrequencia
def main():
  # Captura o texto que deseja analisar
  textoCapturado = input("Digite o texto que deseja analisar: ")
  # Realiza a análise de frequência textual
  contadorDeTokens, contadorDeTipos, frequenciaDeTokens = AnalisadorDeFrequenciaTextual(textoCapturado)
  # Imprime os resultados
  print("Número total de tokens:", contadorDeTokens)
  print("Número total de types:", contadorDeTipos)
  print("\nFrequência dos tokens:")
  for token, frequency in frequenciaDeTokens.items():
      print(f"{token}: {frequency}")
if __name__ == "__main__":
  main()