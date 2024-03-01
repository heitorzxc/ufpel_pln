# Sem utilizar métodos explícitos de remoção, na string unificada do exercício anterior, mantenha apenas a primeira e a última strings incial
# Início do código anterior
# Escreva um programa que inicialize três strings distintas, e na sequência unifique-as
fraseA = input('Digite uma frase: ')
fraseB = input('Digite uma frase: ')
fraseC = input('Digite uma frase: ')
# Ambiguidade. É para concatenar ou espaçar e tornar as três frases uma coisa só?
uniaoFrases = fraseA + fraseB + fraseC
# print('A união das frases é:' + uniaoFrases)
# Fim do código anterior
# Trabalhar em cima do uniaoFrases.
# https://docs.python.org/pt-br/3/library/stdtypes.html#str.rsplit
# Poderia usar o split para fatiar usando o # como delimitador, mas como não posso usar métodos de remoção, vou ter que fazer varredura.
print(uniaoFrases[:len(fraseA)] + uniaoFrases[len(fraseA+fraseB):])
# O jeito foi usar o deslocamento calculando dentro do uniaoFrases e ir usando os delimitadores[xx:yy] que foram usados em sala de aula!