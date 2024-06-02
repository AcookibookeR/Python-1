#MÓDULOS E BIBLIOTECAS EM PYTHON
#Um módulo é um arquivo contendo definições e instruções Python que podem ser importadas e utilizadas em outros programas.
# import "biblioteca" (importa tudo) // from "biblioteca" import "o que eu quero" (importa somente o que eu necessito) poupa memória

import random
from math import factorial

num = random.randint(1,15) #random.randint() sorteia um numero aleatorio se não especificar, se (1,15) ele sorteia entre 1 e 15, não mais e nem menos.

num1 = int(input("Digite um número: "))

fatorial = factorial(num1)
print(fatorial)

print(num)



