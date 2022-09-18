# Antonio Claudio Teixeira Alves

# Faça um progrsms que leia 10 inteiros e imprima sua média.

sum = 0

for i in range(10):
    values = int(input(f"Digite a {i + 1}º nota: "))
    sum += values

print(f"A média é {sum/10}")
