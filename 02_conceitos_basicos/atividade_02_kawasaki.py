# EXERCÍCIO 02: Consumo da Kawasaki Versys 300
# Disciplina: Lógica de Programação com Python

# ENUNCIADO:
# Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
# solicite:
# 1. A distância total percorrida (em Km).
# 2. O total de combustível gasto (em Litros).

# Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
# """
distancia = float (input("digite a distancia percorrida:"))
combustivel = float (input("o total de combustivel gastos:(em litros)")) 
consumo_medio = distancia / combustivel
print(f"o consumo medio da motocicleta e de:{consumo_medio:.2f} km/l")
               

                  