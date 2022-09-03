# Antonio Claudio Teixeira Alves

# Faça um Programa que peça as quatro notas
# de 10 alunos, calcule e armazene em uma lista
# a média de cada aluno, imprima o número de alunos
# com média maior ou igual a 7.0

notas_de_alunos = []
medias_dos_alunos = []
quantidade_de_aluno = 3
soma = 0
aprovados = 0

for i in range(0, quantidade_de_aluno, 1):
    print("")
    print(f"Notas do aluno {i + 1}")
    notas = []
    for j in range(0, 4, 1):
        notas.append(float(input(f"Nota {j + 1}: ")))
        soma += notas[j]

    notas_de_alunos.append(notas)
    medias_dos_alunos.append(soma)
    soma = 0

print("")
for i in range(0, quantidade_de_aluno, 1):
    if (medias_dos_alunos[i] / 4) >= 7:
        print(notas_de_alunos[i])
        aprovados += 1

print(f"Foram aprovado {aprovados} alunas(os)")