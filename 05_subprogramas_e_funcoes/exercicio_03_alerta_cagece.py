"""
EXERCÍCIO 03: Gerador de Alertas da Cagece
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Desenvolva um procedimento `emitir_alerta_fatura(nome_cliente, valor, data_vencimento)`
que imprima a mensagem:
"Prezado(a) [nome], sua fatura da Cagece no valor de R$ [valor] vence no dia [data]."
"""

# TODO: Desenvolva o procedimento abaixo:
def emitir_alerta_fatura(nome_cliente, valor, data_vencimento):
    # O procedimento apenas imprime a mensagem formatada na tela
    print(f"Prezado(a) {nome_cliente}, sua fatura da Cagece no valor de R$ {valor:.2f} vence no dia {data_vencimento}.")

# Exemplo de como chamar o procedimento no seu código:
emitir_alerta_fatura("Lorrana", 1400, "7/07/2027")