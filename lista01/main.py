# Aluno: Antonio Claudio Teixeira Alves

# Leia o salário de um funcionário. Calcule e imprima o valor do novo salário,
# sabendo que ele recebeu um aumento de 25%

print("Digite seu sálario: ", end="")
salary = float(input())
new_salary = (salary * 25 / 100) + salary

print("Parabéns você acabar de ganhar um aumento de 25%")
print(f"Seu novo salário é {new_salary}")