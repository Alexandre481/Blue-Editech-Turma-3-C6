###Exerc 2 Tuplas 16-06
# 02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.

num = (int(input('1º valor:')), int(input('2º valor:')), int(input('3º valor:')), int(input('4º valor:')))
print(num)
print(f'O número 9 aparece {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 foi digitado pela primeira vez na posição {num.index(3)}')
else:
    print('O número 3 não foi digitado')


       