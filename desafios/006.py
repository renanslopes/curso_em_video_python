#  PARTE INTEIRA DE UM NÚMERO
#import math
from math import trunc
numero = float(input('Informe o número a ser retornada sua parte inteira: '))
print('A parte inteira de {} é: {}'.format(numero, trunc(numero)))
# Segunda maneira de ser feita
print('A parte inteira de {} é: {}'.format(numero, int(numero)))
