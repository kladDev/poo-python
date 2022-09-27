# Antonio Claudio Teixeira Alves

# Crie uma função que recebe como parâmetro
# um número inteiro e devolve o seu dobro.

def separador():
    print("-"*15)

def double(value):
    return value * 2

separador()
print("\tDOBRO")
separador()

value = int(input("Digite o valor: "))
value = double(value)
print(f"Seu dobro é {value}")
