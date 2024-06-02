#converter C para F
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) / 1.8
print(f"A temperatura atual em Celsius é de: {celsius} ")

celsius2 = float(input("Digite a temperatura em celsius: "))
fahrenheit2 = (1.8 * celsius2) + 32
print(f"A temperatura atual em Fahrenheit é de: {fahrenheit2}")