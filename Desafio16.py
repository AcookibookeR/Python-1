#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos 
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Digite quantos dias você utilizou o automóvel: "))
km = float(input("Digite quantos quilometros foram rodados: "))
alugel = (dias * 60) + km * 0.15
print(f"O total final do aluguel do automóvel X foi de {alugel:.2f}")