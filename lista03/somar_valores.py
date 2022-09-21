# Antonio Claudio Teixeira Alves

# Faça um programa que peça ao usuário para digitar 10 valores e some-os

sum = 0

for i in range(10):
    values = float(input(f"Digite {i+1}º valor: "))
    sum += values

print(f"A soma é {sum:.2f}")
