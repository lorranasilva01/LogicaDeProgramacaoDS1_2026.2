"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo
x = int(input("digite o valor da inicial"))
y = int(input("digite o valor final"))
inicio = min(x , y)
fim = max (x  , y)
for num in range(inicio, fim + 1):
    if num % 5 == 2 or num % 5 == 3:
        print(num)