r1 = float(input("Digite o valor de r1: "))
r2 = float(input("Digite o valor de r2: "))
r3 = float(input("Digite o valor de r3: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("As três retas formam um triângulo.")
else:
    print("As três retas não formam um triângulo.")