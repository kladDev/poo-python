# Antonio Claudio Teixeira Alves

# Escreva um algoritmo que leia certa quantidade de números e imprima
# o maior deles e quantas vezes o maior valor número foi lido. A quan-
# tidade de números a serem lidos deve ser fornecida pelo usuário.

def separador():
    print("-"*20)

separador()
print("Maior Número")
separador()

number_quantity = int(input("Deseja digitar quantos números? "))
times_read_biggest = 0


for i in range(0, number_quantity, 1):
    value = int(input(f"Digite o {i+1}º valor: "))

    if i == 0:
        biggest_number = value

    if value > biggest_number:
        biggest_number = value
        times_read_biggest += 1

print(f"O maior valor é {biggest_number} e foi lido {times_read_biggest}")
