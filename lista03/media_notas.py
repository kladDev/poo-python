# Antonio Claudio Teixeira Alves

# Faça um progrsms que leia 10 inteiros e imprima sua média.

soma = 0

for i in range(0, 10, 1):
    valores = int(input(f"Digite a {i + 1}º nota: "))
    soma += valores

print(f"A média é {soma/10}")