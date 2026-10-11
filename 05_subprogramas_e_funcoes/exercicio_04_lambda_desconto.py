"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:
desconto_avista = lambda valor: valor * 0.85
print("casas paulino - desconto a vista")
valor_produto = float(input("digite o valor do produto (R$):"))
valor_final = desconto_avista(valor_produto)
print (F"valor com 15% de desconto a vista: R$ {valor_final:.2f}")