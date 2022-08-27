# Antonio Claudio Teixeira Alves

# Receba o salário-base de um funcionário. Calcule e imprima o salário a
# receber, sabendo-se que esse funcionário tem uma gratificação de 5%
# sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário base.

print("Digite seu salário-base R$ ", end="")
base_salary = float(input())
gratification = base_salary * 0.05
tax = base_salary * 0.07
salary = base_salary + gratification - tax

print(f"Seu salário será R$ {salary:.2f}")