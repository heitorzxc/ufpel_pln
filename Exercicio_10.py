# Escreva um programa que inicialize três strings distintas, e na sequência unifique-as em uma nova variável. Sem utilizar métodos explícitos de remoção, na string unificada anteriormente, mantenha apenas a primeira e a última string inicialmente inseridas.
string1 = '1 - Em um algoritmo brilhante, as soluções se revelam como o sol da inovação, iluminando o caminho da computação.'
string2 = '2 - A brisa da criatividade sopra suavemente, acariciando linhas de código e criando uma atmosfera de progresso na era digital.'
string3 = '3 - As estrelas do conhecimento cintilam no céu da mente, revelando a vastidão do universo computacional, onde a curiosidade é a verdadeira constelação.'
stringUnica = string1 + string2 + string3
# Splitado para poder usar os delimitadores[:]
stringUnica.split()
# Tamanho captura até o fim da primeira + captura da soma da primeira com a segunda em diante
stringUnica = stringUnica[:len(string1)] + "\n" + stringUnica[len(string1+string2):]
print(str(stringUnica))