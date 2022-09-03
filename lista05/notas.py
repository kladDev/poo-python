# Antonio Claudio Teixeira Alves

# Faça um Programa que leia 4 notas, adicione
# em uma lista e mostre as notas e a média na tela.

def separador():
    print("-"*25)

notas = []
soma = 0

separador()
print("Sistema de notas escolar")
separador()
print("Digite 4 notas abaixo")

for i in range(0, 4, 1):
    notas.append(float(input(f"Nota 0{i + 1}: ")))
    soma += notas[i]

print("")
print(notas)
print(f"A média é {soma/len(notas)}")