# Antonio Claudio Teixeira Alves

# Crie uma função que recebe como parâmetro
# um número inteiro e devolve o seu dobro.

def separador():
    print("-"*15)

def dobro(valor):
    return valor * 2

separador()
print("\tDOBRO")
separador()

valor = int(input("Digite o valor: "))
valor = dobro(valor)
print(f"Seu dobro é {valor}")