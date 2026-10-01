"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
quantidade_positivo = 0
soma_positivo = 0.0
for i in range(6):
    valor = float(input(f"digite o {i+1} valor:"))
    if valor > 0:
        quantidade_positivo += 1
        soma_positivo += valor
        print(f"{quantidade_positivo} valores positivo")
        if quantidade_positivo > 0:
            media = soma_positivo/ quantidade_positivo
            print(f"{media:.1f}")