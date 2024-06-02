vel = float(input("Digite a velocidade: "))
if vel > 80:
    print("Você foi multado!")
    print("O valor de cada Km acima do limite é de R$ 7.00")
    passou_km = vel - 80
    multa = (vel - 80) * 7
    print(f"Você atingiu a velocidade de {vel}km/h, ultrapassando {passou_km}km/h e terá de pagar o total de R$ {multa} .")
else:
    print("Você não foi multado!")