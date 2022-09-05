# Antonio Claudio Teixeira Alves

# Faça uma função para verificar se um
# número é positivo ou negativo. Sendo
# que o valor de retorno será 1 se positivo,
# -1 se negativo e O se for igual a 0.

def separador():
    print("-"*20)

def verificar_numero(valor):
    if valor == 0:
        return 0
    elif valor > 0:
        return 1
    else:
        return -1

separador()
print("Verificar de numero")
separador()

valor = int(input("Digite um valor: "))
valor = verificar_numero(valor)
print(f"O retorno é {valor}")