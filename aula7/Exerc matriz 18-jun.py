#### Crie um programa que declare uma matriz de dimensão 3×3
#  e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com essa formatação:
# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# [  7  ][  8  ][  9  ] 
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('Digite o valor: ')) 
        linha.append(valor)
    matriz.append(linha)

print(matriz)

for i in matriz:
    print()
    for j in i:
        print(f'   [ {j} ]', end='')