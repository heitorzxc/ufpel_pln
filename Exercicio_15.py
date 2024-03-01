# Uso de Expressões Regulares: Use expressões regulares para encontrar todas as ocorrências das palavras "João" e "Maria", inclusive como subpalavras, na história e destaque essas palavras no texto, reescrevendo-as com todas as letras maiúsculas.
import re
frase = 'Joãozinho e Maria, dois irmãos aventureiros, decidiram explorar a floresta misteriosa próxima à sua casa. A floresta era densa, com árvores altas e folhagem espessa. Enquanto caminhavam, João e Maria encontraram pegadas estranhas no chão e decidiram segui-las. As pegadas os levaram a uma clareira onde descobriram uma casa feita inteiramente de doces! Ficaram fascinados e não resistiram à tentação de experimentar os doces. Mas, assim que começaram a comer, uma bruxa má e enrugada apareceu. A bruxa riu de forma maligna e os assustou. Joãozinho e Maria, apavorados, deixaram os doces e fugiram da casa. A bruxa tentou segui-los, mas eles eram ágeis e conseguiram escapar. Finalmente, após uma longa e cansativa jornada, João e Maria voltaram em segurança para sua casa, onde prometeram nunca mais se aventurar naquela floresta perigosa.'
destacar = ['João', 'Maria']
# https://docs.python.org/3/library/re.html
# Expressão regular:
# \b - bounds - limites - bordas da palavra
# Expressão regular:
# Capturando as bordas de cada palavra.
# Obtendo o mapeamento do que deve escapar e do que deve destacar.
# Ignorando maiúsculas e minúsculas.
# Como visto em linguagens formais, w* é o fecho de w, podendo ser qualquer coisa, inclusive vazio.
padrao = re.compile(r'\b(?:' + '|'.join(map(re.escape, destacar)) + r')\w*\b', re.IGNORECASE)
# Fazendo a substituição da string por meio dos argumentos  dados pela passagem de parâmetros
# Se deu match com a regra, é feita a capitalização, senão, segue adiante com a frase
frase = padrao.sub(lambda match: match.group(0).upper(), frase)
# Imprime o texto modificado
print(frase)