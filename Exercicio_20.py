# Pesquise como utilizar o Word2Vec (Biblioteca GenSim do Python) e crie um modelo Word2Vec para um corpus de sua escolha.
pip install wikipedia unidecode spacy matplotlib
python -m spacy download pt_core_news_sm

import wikipedia
import spacy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Definindo o idioma da Wikipédia para português e buscando conteúdo
wikipedia.set_lang('pt')
busca = input('Digite o que deseja buscar na Wikipédia: ')

try:
    pagina = wikipedia.page(busca)
    conteudo = pagina.content
    print('Busca realizada, iniciando processamento do texto.')
except wikipedia.exceptions.DisambiguationError as e:
    print("Por favor, seja mais específico. Possíveis significados:")
    for option in e.options:
        print(option)
    exit()
except wikipedia.exceptions.PageError:
    print("A página solicitada não foi encontrada.")
    exit()

# Carrega o modelo de linguagem do spaCy
nlp = spacy.load('pt_core_news_sm')

# Processa o texto com spaCy
doc = nlp(conteudo)

# Filtra tokens baseado em critérios: não são stopwords, são alfabéticos e não são pontuações
tokens_lematizados_unicos = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]

# Remoção de duplicatas mantendo a ordem
tokens_lematizados_unicos = list(dict.fromkeys(tokens_lematizados_unicos))

# Processando os tokens únicos para extrair vetores
doc = nlp(' '.join(tokens_lematizados_unicos))
vetores = np.array([token.vector for token in doc if token.has_vector])

# Redução de dimensionalidade e plotagem
tsne = TSNE(n_components=2, random_state=0)
tokens_reduzidos = tsne.fit_transform(vetores)

plt.figure(figsize=(12, 12))
for i, token in enumerate(doc):
    if token.has_vector:
        plt.scatter(tokens_reduzidos[i, 0], tokens_reduzidos[i, 1])
        plt.text(tokens_reduzidos[i, 0], tokens_reduzidos[i, 1], token.text, fontsize=9)
plt.show()