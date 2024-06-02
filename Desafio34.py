salarium = float(input("Digite o valor de seu salário: "))

if salarium > 1250:
    aumento1 = (1250 * 10) / 100
    salarium += aumento1
    print(f"Seu novo salário com aumento de 10% é de: R$ {salarium} .")
else:
    aumento2 = (salarium * 15) / 100
    salarium += aumento2
    print(f"Seu novo salário com aumento de 15% é de: R$ {salarium} .")