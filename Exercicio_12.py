# Tokenização: Divida a história em palavras individuais.
# pip install nltk
import string
# Bom exercício, pois já posso eliminar as vírgulas dividir a história em PALAVRAS INDIVIDUAIS.
entrada = 'Joãozinho e Maria, dois irmãos aventureiros, decidiram explorar a floresta misteriosa próxima à sua casa. A floresta era densa, com árvores altas e folhagem espessa. Enquanto caminhavam, João e Maria encontraram pegadas estranhas no chão e decidiram segui-las. As pegadas os levaram a uma clareira onde descobriram uma casa feita inteiramente de doces! Ficaram fascinados e não resistiram à tentação de experimentar os doces. Mas, assim que começaram a comer, uma bruxa má e enrugada apareceu. A bruxa riu de forma maligna e os assustou. Joãozinho e Maria, apavorados, deixaram os doces e fugiram da casa. A bruxa tentou segui-los, mas eles eram ágeis e conseguiram escapar. Finalmente, após uma longa e cansativa jornada, João e Maria voltaram em segurança para sua casa, onde prometeram nunca mais se aventurar naquela floresta perigosa.'
# Princípio OO do exercício 4 aplicado recursivamente aqui:
# Estou dividindo a string usando espaços como delimitador e removendo espaços extras (default)
entrada = ' '.join(entrada.split())
# Ainda tenho um problema: Pontuação. O exercício me pede as palavras individuais.
# Perceba que posso chamar vários métodos dentro do Python, assim, economizo linhas.
entrada = entrada.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace(':', '')
print (entrada)