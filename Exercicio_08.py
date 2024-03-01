# Solicite ao usuário que insira uma frase. Seu programa deve inverter a ordem das palavras na frase e exibi-la de trás para frente. Por exemplo, se o usuário inserir "Python é divertido", o programa deve exibir "divertido é Python". Remova espaços extras contidos na frase, se houver
import string
frase = input("Digite uma frase: ")
# split() divide a string em uma lista de substrings usando espaços em branco como delimitadores. Por padrão, a função split() remove espaços em branco adicionais entre as palavras.
frase = frase.split()
# Agora como tenho uma lista, posso fazer o reverso dela (inverter as palavras) --- atenção que é um método sem retorno!!
frase.reverse()
# join() é usado para unir os elementos de uma lista em uma única string. Neste caso, estamos usando um espaço em branco como o caractere de junção (à esquerda da chamada). O resultado é uma string em que os espaços duplicados foram removidos.
frase = ' '.join(frase)
# Imprimindo a string invertida sem os caractereres em branco extras.
print (frase)