# Antonio Claudio Teixeira Alves

# Faça um programa que determine e mostre os cinco primeiros
# múltiplos de 3, considerando números maiores que 0

multiplo_3 = 0
i = 0

while multiplo_3 <= 5:
    i += 1
    if i % 3 == 0:
        print(i)
        multiplo_3 += 1



