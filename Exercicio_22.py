# Desambiguação semântica de palavras

pip install nltk googletrans==4.0.0-rc1
import nltk
from nltk.corpus import wordnet as wn
from googletrans import Translator

nltk.download('wordnet')
nltk.download('omw-1.4')

def traduzir(texto):
  tradutor = Translator()
  def_idiomas = tradutor.translate(texto, src='en', dest='pt')
  return def_idiomas.text

def desambiguar(palavra):
  significados = []
  
  # Busca os synsets (conjuntos de sinônimos) para a palavra
  for syn in wn.synsets(palavra, lang='por'):
    definicao = syn.definition()
    exemplos = syn.examples()
    
    # Traduz a definição e os exemplos para o português
    definicao_pt = traduzir(definicao)
    exemplos_pt = [traduzir(exemplo) for exemplo in exemplos]
    
    significados.append((definicao_pt, exemplos_pt))
  
  return significados

# Exemplo 1
desambiguar("manga")

# Exemplo 2
desambiguar("banco")

# Exemplo 3
desambiguar("letra")
