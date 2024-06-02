phrase = str(input("Digite uma frase: ")).strip().upper()
print(f"A letra \"A\" aparece {phrase.count('A')}")
print(f"A letra \"A\" aparece pela primeira vez no index {(phrase.find('A')+1)}") 
#aqui começou a analisar da esquerda p/ direita.
print(f"A letra \"A\" aparece pela última vez no index {(phrase.rfind('A')+1)}")
#aqui começou a analisar da direita p/ esquerda.