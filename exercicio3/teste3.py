import json

# Função simplificada para calcular os dados de faturamento
def calcular_faturamento(dados):
    faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]
    return min(faturamentos), max(faturamentos), sum(1 for f in faturamentos if f > sum(faturamentos) / len(faturamentos))

# Suponha que os dados de faturamento venham de uma fonte externa (ex: um arquivo JSON)
with open('faturamento.json', 'r') as f:
    dados_faturamento = json.load(f)

# Calcular e exibir resultados
menor, maior, dias_acima_media = calcular_faturamento(dados_faturamento)
print(f"Menor faturamento: R${menor:.2f}")
print(f"Maior faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
