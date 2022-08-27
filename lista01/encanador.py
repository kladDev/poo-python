# Antonio Claudio Teixeira Alves

# Uma empresa contrata um encanador a R$ 30,00 por dia.
# Faça um programa que solicite o número de dias trabalhadas pelo encanador
# e imprima a quantia líquida que deverá ser paga, sabendo-se que são
# descontados 8% para imposto de renda.

print("Olá, bem-vindo ao cargo de encanador")
print("Quantos dias irá trabalhar? dias: ", end="")
quantity_day = int(input())
salary = quantity_day * 30 - (quantity_day * 30 * 8 / 100)

print(f"Seu salário é {salary:.2f}")

