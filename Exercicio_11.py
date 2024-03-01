# Peça ao usuário para inserir uma frase. Seu programa deve encontrar e exibir a palavra mais longa na frase. Você pode considerar que as palavras são separadas por espaços em branco. Por exemplo, se o usuário inserir "Python é uma linguagem de programação poderosa", o programa deve exibir "programação" como a palavra mais longa.
import string
# Bom exercício! O iterador é passadom, != do C/C++ em que o iterador é criado.
# O método str.len() retorna o tamanho, e posso guardar O ITERADOR cujo maior valor.
# Entretanto, vou ter que splitar usando o espaço como delimitador em uma lista.
# frase = 'Python é uma linguagem de programação poderosa'.split(' ')
frase = input("Digite uma frase: ").split(' ')
# Princípio OO: Se input retorna str, nada impede de str.split(' ') ser o retorno.
# Aqui tenho uma lista ['Python', 'é', ... , 'poderosa'].
# Posso iterar e armazenar o conteúdo da lista.
maiorPalavra = ''
for i in frase :
  if len (maiorPalavra) < len(i) :
    maiorPalavra = i
# Varredura na frase verificando o tamanho de cada palavra, sempre substituindo pela maior.
print("Maior palavra: " + str(maiorPalavra))
# Perfeito, retornou que a maior palavra é "programação", agora no debug eu posso trocar a frase pelo input do usuário.