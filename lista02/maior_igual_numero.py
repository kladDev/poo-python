# Antonio Claudio Teixeira Alves

#  Faça um programa que receba dois números e mostre o maior.
#  Se por acaso, os dois números forem iguais, imprima a
#  mensagem Números iguais.

def separador():
    print("-"*25)

separador()
print("\tMaior numero")
separador()

number_one = float(input("Valor 01: "))
number_two = float(input("Valor 02: "))

if number_one > number_two:
    print(f"O maior valor é {number_one}")
elif number_one < number_two:
    print(f"O maior valor é {number_two}")
else:
    print("Os números são iguais")
