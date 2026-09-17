# EXERCÍCIO 03: Conta do Nagoya Sushi House
# Disciplina: Lógica de Programação com Python

# ENUNCIADO:
# Crie um programa que:
# 1. Leia o valor total consumido no restaurante (em R$).
# 2. Aplique a taxa de 10% de serviço do garçom.
# 3. Exiba o valor final da conta a pagar com mensagem formatada.
# """
valor_consumo = float(input("digite o valor total consumido (R$):"))
taxa_de_servico = valor_consumo *(10/100)
valor_final = valor_consumo+taxa_de_servico
print ("o valor final:", valor_final)
