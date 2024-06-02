from math import sqrt
import math
catOp = float(input("Digite o valor do cateto oposto: "))
catAd = float(input("Digite o valor do cateto adjacent: "))
hip = catOp ** 2 + catAd ** 2
res = sqrt(hip)
print(f"A hipotenusa do triângulo A, com cateto oposto de {catOp} metros e cateto adjacente de {catAd} metros é igual a {res:.2f} metros.")
#Ou poderia usar a função math.hypot
 