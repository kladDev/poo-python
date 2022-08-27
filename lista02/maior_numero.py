# Antonio Claudio Teixeira Alves

# Escreva um programa que, dados dois números inteiros, mostre
# na tela o maior deles, assim como a diferença existente entre
# ambos.

def separador():
    print("-"*25)

separador()
print("Maior numero")
separador()

number_one = int(input("Valor 01: "))
number_two = int(input("Valor 02: "))

if number_one > number_two:
    bigger_number = number_one
else:
    bigger_number = number_two

print(f"O maior valor é {bigger_number}")

