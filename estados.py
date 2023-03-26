faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

#somando todos os dados de faturamento de cada estado
total = sum(faturamento.values())

#cálculo do percentual
percentuais = {estado: faturamento / total * 100 for estado, faturamento in faturamento.items()}

# exibindo os resultados percentuais de representação de cada estado. O :.2f para ser exibido apenas com duas casas decimais.
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")