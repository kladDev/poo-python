# Antonio Claudio Teixeira Alves

# Faça um programa que peça ao usuário para digitar 10 valores e some-os

soma = 0

for i in range(0, 10, 1):
    valores = float(input(f"Digite {i+1}º valor: "))
    soma += valores

print(f"A soma é {soma:.2f}")