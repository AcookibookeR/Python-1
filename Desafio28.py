import random
num = random.randint(0,5)
tent = int(input("Digite seu palpite: "))
if tent == num:
    print("Você acertou!")
else:
    print("Você errou!")