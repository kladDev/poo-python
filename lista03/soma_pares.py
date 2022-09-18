# Antonio Claudio Teixeira Alves

# Faça um programa que calcule e mostre a soma dos
# 50 primeiros números pares

i = 0
number_pairs = 0
sum_values = 0

while number_pairs <= 50:
    i += 1
    if i % 2 == 0:
        print(i, end=" ")
        number_pairs += 1
        sum_values += i
print("")
print(f"A soma dos 50 primeiros números pares é {number_pairs}")
