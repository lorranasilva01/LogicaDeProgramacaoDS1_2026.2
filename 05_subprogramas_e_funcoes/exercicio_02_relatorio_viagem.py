"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km, consumo_km, preco_combustivel):
    # Garante que o retorno seja um cálculo numérico
    return (distancia_km / consumo_km) * preco_combustivel

def calcular_custo_alimentacao(pessoas, tempo, alimentacao):
    # Garante que o retorno seja um cálculo numérico
    return pessoas * tempo * alimentacao

print("--- dados do transporte ---")
distancia = float(input("digite a distancia da viagem em km: "))
consumo = float(input("digite o consumo em (km/l): "))
preco_litro = float(input("digite o preco do combustivel por litro: R$ "))

print("\n--- dados da alimentacao ---")
qtd = int(input("digite a quantidade de pessoas: "))
tempo = int(input("digite a quantidade de dias da viagem: "))
alimentacao = float(input("digite o valor da diaria de alimentacao por pessoa: R$ "))

# As funções abaixo vão processar os números e retornar um float
custo_viagem_transporte = calcular_custo_transporte(distancia, consumo, preco_litro)
custo_viagem_alimentacao = calcular_custo_alimentacao(qtd, tempo, alimentacao)
custo_total = custo_viagem_transporte + custo_viagem_transporte + custo_viagem_alimentacao

print(f"custo transporte R$: {custo_viagem_transporte:.2f}")
print(f"custo alimentacao R$: {custo_viagem_alimentacao:.2f}")
print(f"CUSTO TOTAL DA VIAGEM R$: {custo_total:.2f}")
