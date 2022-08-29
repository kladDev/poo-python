# Antonio Claudio Teixeira Alves

# Faça um programa que calcule e mostre a soma dos
# 50 primeiros números pares

i = 0
quantidade_pares = 0
somar_valores = 0

while quantidade_pares <= 50:
    i+=1
    if i % 2 == 0:
        print(i, end=" ")
        quantidade_pares += 1
        somar_valores += i
print("")
print(f"A soma dos 50 primeiros números pares é {somar_valores}")