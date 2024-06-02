num = str(input("Digite um número: "))
tamanho = (len(num))

if tamanho == 4:
    milenio = print("Milênio(s): ",num[0])
    centena = print("Centena(s): ",num[1])
    dezena = print("Dezena(s): ",num [2])
    unidade = print("Unidade(s): ",num [3])
elif tamanho == 3:
    centena = print("Centena(s): ",num[0])
    dezena = print("Dezena(s): ",num [1])
    unidade = print("Unidade(s): ",num [2])
elif tamanho == 2:
    dezena = print("Dezena(s): ",num [0])
    unidade = print("Unidade(s): ",num [1])
elif tamanho == 1:
    unidade = print("Unidade(s): ",num [0])