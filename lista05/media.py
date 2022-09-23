# Antonio Claudio Teixeira Alves

# Faça um Programa que peça as quatro notas
# de 10 alunos, calcule e armazene em uma lista
# a média de cada aluno, imprima o número de alunos
# com média maior ou igual a 7.0

student_grades = []
student_averages = []
quantity_student = 3
sum = 0
approved = 0

for i in range(quantity_student):
    print("")
    print(f"Notas do aluno {i + 1}")
    grades = []
    for j in range(0, 4, 1):
        grades.append(float(input(f"Nota {j + 1}: ")))
        sum += notas[j]

    student_grades.append(notas)
    student_averages.append(soma)
    sum = 0

print("")
for i in range(quantity_student):
    if (student_averages[i] / 4) >= 7:
        print(student_grades[i])
        approved += 1

print(f"Foram aprovado {approved} alunas(os)")
