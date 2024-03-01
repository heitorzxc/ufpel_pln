# Crie um programa que leia uma string fornecida pelo usuário e imprima o comprimento desta
import string
# print("Digite uma frase: ")
# Desprezado pois o print gera quebra de linha, o que não quero.
frase = input("Digite uma frase: ")
# https://docs.python.org/pt-br/3.9/library/2to3.html?highlight=input#2to3fixer-input
# len (frase) recebe a string e retorna o comprimento (int).
# int não pode ser concatenado com strings, portanto converto para string.
# https://docs.python.org/pt-br/3.9/library/stdtypes.html?highlight=str#str
# str () recebe o inteiro e transforma em string para estar concatenado no print.
print("Sua frase é: " + frase)
print("O comprimento da frase é de " + str(len(frase)) + " caracteres.")