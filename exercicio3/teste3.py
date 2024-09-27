import json

def calcular_faturamento(dados):
    faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]
    return min(faturamentos), max(faturamentos), sum(1 for f in faturamentos if f > sum(faturamentos) / len(faturamentos))

with open('C:/Users/rafae/OneDrive/Documentos/Teste_estagio_SP/exercicio3/faturamento.json', 'r') as f:
    dados_faturamento = json.load(f)

menor, maior, dias_acima_media = calcular_faturamento(dados_faturamento)
print(f"Menor faturamento: R${menor:.2f}")
print(f"Maior faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
