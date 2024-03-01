# pip install beautifulsoup4 pandas

from bs4 import BeautifulSoup
import pandas as pd

# O método open abre um arquivo e retorna um objeto do tipo file.
# O parâmetro 'r' indica que o arquivo será aberto para leitura.
# O parâmetro encoding indica a codificação do arquivo.

with open("exemplo.html", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Fazer o parsing do HTML com o BeautifulSoup
# O método BeautifulSoup cria uma árvore de análise a partir do conteúdo HTML.
# Uma árvore de análise é uma estrutura de dados que representa o conteúdo do HTML.
# O parâmetro 'html.parser' indica que o parser a ser utilizado é o HTML parser.
# O parser é um programa que lê o conteúdo HTML e o transforma em uma árvore de análise.
# O BeautifulSoup é uma biblioteca que facilita a extração de informações de uma árvore de análise.

soup = BeautifulSoup(conteudo, 'html.parser')

# Extrair informações das tags <article>.
# A tag <article> contém o título e a descrição de um artigo.
# O método find_all retorna uma lista com todas as ocorrências de uma tag que satisfaça os critérios especificados.
# Find_all retorna uma lista vazia se não encontrar nenhuma ocorrência da tag.

artigos = soup.find_all('article')

# Criar uma lista para armazenar os dados dos artigos.
# Cada elemento da lista será um dicionário com os dados de um artigo
# Cada dicionário terá as chaves 'Título' e 'Descrição' e os valores correspondentes
# A lista será preenchida com os dados de todos os artigos.

dados_artigos = []

# Para cada artigo, extrair o título e a descrição e adicionar à lista de dados.
# O método find retorna a primeira ocorrência de uma tag que satisfaça os critérios especificados.
# O método text retorna o texto contido na tag.
# O método strip remove os espaços em branco do início e do fim do texto.
# O método append adiciona um elemento ao final de uma lista.

for artigo in artigos:
  titulo = artigo.find('h3').text.strip()
  descricao = artigo.find('p').text.strip()
  dados_artigos.append({'Título': titulo, 'Descrição': descricao})

# O DataFrame é como uma tabela, onde cada linha é um artigo e cada coluna é um atributo do artigo.
# O método pd.DataFrame cria um DataFrame a partir de uma lista de dicionários.
# Cada dicionário na lista corresponde a um artigo, onde as chaves são os nomes das colunas e os valores são os dados do artigo.

df = pd.DataFrame(dados_artigos)

# Apresentar os dados do DataFrame na tela, para verificar se a extração foi feita corretamente.
print(df)