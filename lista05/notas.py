# Antonio Claudio Teixeira Alves

# Faça um Programa que leia 4 notas, adicione
# em uma lista e mostre as notas e a média na tela.

def separador():
    print("-"*25)

grades = []
sum = 0

separador()
print("Sistema de notas escolar")
separador()
print("Digite 4 notas abaixo")

for i in range(0, 4, 1):
    grades.append(float(input(f"Nota 0{i + 1}: ")))
    sum += grades[i]

print("")
print(grades)
print(f"A média é {sum/len(grades)}")
