'''
Tema: Verificar para determinada entrada o impacto médio de indicadores emocionais e sua popularidade.
Corpus: Banco de Dados de Notícias da Reuters.
'''

import nltk
from nltk.corpus import reuters
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import defaultdict
import matplotlib.pyplot as plt

nltk.download('reuters')
nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

def analyze_emotional_coverage_with_pep(corpus, termo_busca):
  termo_convergencia = defaultdict(lambda: defaultdict(int))
  total_documentos = 0
  for file_id in corpus.fileids():
    text = corpus.raw(file_id)
    if termo_busca.lower() in text.lower():
      total_documentos += 1
      sentimento = sid.polarity_scores(text)
      if sentimento['compound'] > 0.05:
          termo_convergencia[file_id]['positive'] += 1
      elif sentimento['compound'] < -0.05:
          termo_convergencia[file_id]['negative'] += 1
      else:
          termo_convergencia[file_id]['neutral'] += 1
  return termo_convergencia, total_documentos

def main():
  termo_busca = input("Digite o termo a ser buscado: ")
  reuters_termo_convergencia, reuters_termo_documentos = analyze_emotional_coverage_with_pep(reuters, termo_busca)
  print("Menções: ", reuters_termo_documentos)
  if reuters_termo_documentos > 0:
    total_positive = sum(emotions['positive'] for emotions in reuters_termo_convergencia.values())
    total_negative = sum(emotions['negative'] for emotions in reuters_termo_convergencia.values())
    total_neutral = sum(emotions['neutral'] for emotions in reuters_termo_convergencia.values())
    print("Positivos:", total_positive)
    print("Negativos:", total_negative)
    print("Neutros:", total_neutral)
    labels = ['Positiva', 'Negativa', 'Neutra']
    frequencies = [total_positive, total_negative, total_neutral]
    plt.bar(labels, frequencies, color=['green', 'red', 'blue'])
    plt.xlabel('Classe Emocional')
    plt.ylabel('Frequência')
    plt.title(f'Distribuição de Frequência da Convergência Emocional para {termo_busca}')
    plt.show()
    max_tendency = max(total_positive, total_negative, total_neutral)
    if max_tendency == total_positive:
        print("Maioria das análises: Positiva.")
    elif max_tendency == total_negative:
        print("Maioria das análises: Negativa.")
    else:
        print("Maioria das análises: Neutra.")
  else:
      print("Termo não encontrado no corpus Reuters.")

if __name__ == "__main__":
  main()
