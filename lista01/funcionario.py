# Antonio Claudio Teixeira Alves

# Faça um programa que leia o valor da hora de trabalho (em reais) e números
# de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário,
# adicionando 10% sobre o valor calculado.

print("Digite o valor da hora de trabalho, R$ ", end="")
hour_value = float(input())
print("Qual a quantidade de horas trabalhadas no mês: ", end="")
hour_worked = int(input())

salary = (hour_worked * hour_value * 10 / 100) + hour_worked*hour_value
print(f"Seu salário será R${salary:.2f}")