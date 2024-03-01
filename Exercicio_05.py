# Escreva um programa que inicialize uma lista com 10 elementos quaisquer e na sequência remova os elementos dos índices 4, 5, e 6.
import random
# https://docs.python.org/pt-br/3.9/library/random.html?highlight=random
lista = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
print (lista)
# Removendo do fim para o começo para não ter que ficar recalculando índices.
lista.pop(6-1)
lista.pop(5-1)
lista.pop(4-1)
# Não tem sinal de igualdade pelo fato da função pop fazer o retorno do item removido e não da lista.
print (lista)