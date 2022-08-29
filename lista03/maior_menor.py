# Antonio Claudio Teixeira Alves

# Escreva um programa que leia 5 números e escreva o menor valor lido
# e o maior valor lido

for i in range(0, 5, 1):
    valores = float(input(f"Digite o {i+1}° valor: "))

    if i == 0:
        menor_valor = valores
        maior_valor = valores

    if menor_valor < valores:
        menor_valor = valores

    if maior_valor > valores:
        maior_valor = valores

print("")
print(f"O maior valor é {maior_valor:.2f}")
print(f"O menor valor é {menor_valor:.2f}")
