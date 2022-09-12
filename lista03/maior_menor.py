# Antonio Claudio Teixeira Alves

# Escreva um programa que leia 5 números e escreva o menor valor lido
# e o maior valor lido

for i in range(5):
    value = float(input(f"Digite o {i+1}° valor: "))

    if i == 0:
        lower_value = value
        bigger_value = value

    if lower_value < value:
        lower_value = value

    if bigger_value > value:
        bigger_value = value

print("")
print(f"O maior valor é {bigger_value:.2f}")
print(f"O menor valor é {lower_value:.2f}")
