#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
#e o último nome separadamente.

name = str(input("Digite seu nome: ")).strip()
n = name.split()
print(n)
print(name)
print("Seu primeiro nome é ",n[0])
print("Seu último nome é ",n[len(n)-1])
#primeiro fiz o split de name, depois o len descobriu o tamanho do split e retirou -1 para retornar o último valor da lista.