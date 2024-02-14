

def calcular_percentual():

    faturamento = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    valor_total = sum(faturamento.values())

    print(f"Faturamento Mensal da Distribuidora: R${valor_total:,.2f}")

    percentuais = {estado: (valor / valor_total) * 100 for estado, valor in faturamento.items()}

    return percentuais


if __name__ == "__main__":
    percentuais = calcular_percentual()

    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")