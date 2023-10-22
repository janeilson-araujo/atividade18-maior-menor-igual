# Exercício Python 18: Escreva um programa que leia dois números
# inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais

print("compare dois números e descubra se são diferentes ou iguais")
numero1 = int(input("insira o primeiro número:"))
numero2 = int(input("insira o segundo número:"))

if numero1 > numero2 :
    print("o primeiro valor é maior")
elif numero1 < numero2 :
    print("o segundo valor é maior")
else :
    print("Não existe valor maior, os dois são iguais")        