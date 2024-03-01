# Faça um programa que receba duas frases distintas e imprima de maneira invertida, trocando as letras A por * e as letras E por +.
import string
fraseA = input('Digite frase 1: ')
fraseB = input('Digite frase 2: ')
# Todos os A || a serão substituídos por @
fraseA = fraseA.replace('A', '@')
fraseA = fraseA.replace('a', '@')
fraseA = fraseA.replace('E', '#')
fraseA = fraseA.replace('e', '#')
# Todos os E || e serão substituídos por #
fraseB = fraseB.replace('A', '@')
fraseB = fraseB.replace('a', '@')
fraseB = fraseB.replace('E', '#')
fraseB = fraseB.replace('e', '#')
# Todos os @ serão substituídos por *
fraseA = fraseA.replace('@', '*')
fraseA = fraseA.replace('#', '+')
# Todos os # serão substituídos por +
fraseB = fraseB.replace('@', '*')
fraseB = fraseB.replace('#', '+')
# Imprimindo as frases de maneira invertida com as trocas já feitas
print('Frase 2: ' + fraseB + ' Frase 1: ' + fraseA)