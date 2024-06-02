dia = int(input("Digite o dia de seu nascimento: "))
mes = str(input("Digite o mês de seu nascimento: "))
ano = int(input("Digite o ano de seu nascimento: "))

print(f"Você nasceu em {dia}/{mes}/{ano}, correto?")
resp = (input(""))
if resp == "sim":
    print("Seja bem-vindo!")
else:
    print("Deseja alterar?")
    input()
