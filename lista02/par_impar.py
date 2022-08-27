# Antonio Claudio Teixeira Alves

# Fça um programa que receba um número inteiro e verifique
# se este númreio é par ou ímpar

def separador():
    print("-"*25)

separador()
print("Verificador de número")
separador()

value = int(input("Digite um número: "))

if(value % 2 == 0):
    print("É par")
else:
    print("É ímpar")