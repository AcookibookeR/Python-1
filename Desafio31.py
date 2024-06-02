km = float(input("Digite o total de quilômetros: "))

if km <= 200:
    preco = 0.50 * km
    print(f"O valor total da viagem, considerando R$ 0.50 por Km rodado, será de: R$ {preco} . ")
else:
    preco2 = 0.45 * km
    print(f"O valor total da viagem, considerando R$ 0.45 por Km rodado, será de: R$ {preco2} . ")