# Remoção de stopwords: Remova as palavras de parada (stopwords) do texto. Você pode usar a lista de stopwords do NLTK ou outra lista de sua escolha.
# pip install nltk
# --- Reaproveitando o código do exercício 5 ---
import string
entrada = 'Joãozinho e Maria, dois irmãos aventureiros, decidiram explorar a floresta misteriosa próxima à sua casa. A floresta era densa, com árvores altas e folhagem espessa. Enquanto caminhavam, João e Maria encontraram pegadas estranhas no chão e decidiram segui-las. As pegadas os levaram a uma clareira onde descobriram uma casa feita inteiramente de doces! Ficaram fascinados e não resistiram à tentação de experimentar os doces. Mas, assim que começaram a comer, uma bruxa má e enrugada apareceu. A bruxa riu de forma maligna e os assustou. Joãozinho e Maria, apavorados, deixaram os doces e fugiram da casa. A bruxa tentou segui-los, mas eles eram ágeis e conseguiram escapar. Finalmente, após uma longa e cansativa jornada, João e Maria voltaram em segurança para sua casa, onde prometeram nunca mais se aventurar naquela floresta perigosa.'
entrada = ' '.join(entrada.split())
entrada = entrada.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace(':', '')
# --- Reaproveitando o código do exercício 5 ---
# Importando o kit de ferramentas de linguagens naturais
import nltk
# Molda o corpo do PLN para detectar stopwords
from nltk.corpus import stopwords
# Prepara o PLN para tokenizar palavras
from nltk.tokenize import word_tokenize
# Faz o download de stopwords - incluindo o português
# https://www.nltk.org/howto/corpus.html?highlight=stopwords
nltk.download('stopwords')
# Faz o download de modelos de tokenização - incluindo o português
# https://www.nltk.org/_modules/nltk/tokenize/punkt.html
nltk.download('punkt')
# Obtém todas as stopwords da língua portuguesa e as encaixa em uma lista
palavrasParada = nltk.corpus.stopwords.words('portuguese')
# Agora preciso fazer a varredura do texto em busca das stopwords
# Lembrando que reaproveitei código do exercício 5 para eliminar pontos e vírgulas
# O exercício 5 abordava sobre tokenização, algo que precisava aqui
# Tokenizando a entrada...
textoTokenizado = word_tokenize(entrada, language='portuguese')
# Verificando se cada token não está presente na lista de stopwords
# O iterador é confrontado de forma que mesmo que formatado ele não pode ser uma palavra de parada
textoVerificado = []
for iterador in textoTokenizado:
    if iterador.lower() not in palavrasParada:
        textoVerificado.append(iterador)
# Tenho como retorno uma lista, preciso que isso vire uma string com espaços separando-as:
textoVerificado = ' '.join(textoVerificado)
# Impressão do texto sem as stopwords.
print (textoVerificado)
# Incrível, removendo as stopwords ainda assim é compreensível a semântica do texto original, economizando memória!