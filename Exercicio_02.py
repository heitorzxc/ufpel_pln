# Escreva um programa que substitui as ocorrências de um caractere 0 em uma string por outro caractere 1.
# Dica: Para o exercício 2, busque na documentação da linguagem um método que possa auxiliar.
import string
# https://docs.python.org/pt-br/3.9/library/stdtypes.html#str.replace
minhaString = "1ss0 é c0m0 em um aut0mat0 0u máqu1na de Tur1ng, 0nde p0ss0 subst1tu1r zer0s p0r uns."
print(minhaString)
minhaString = minhaString.replace('0', 'X')
minhaString = minhaString.replace('1', 'Y')
minhaString = minhaString.replace('X', '1')
minhaString = minhaString.replace('Y', '0')
print(minhaString)