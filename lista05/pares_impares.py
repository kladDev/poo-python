# Antonio Claudio Teixeira Alves

# Faça um Programa que leia 20 números inteiros
# e armazene-os uma lista. Armazene os números
# pares na lista PAR e os números IMPARES na lista
# impar. Imprima as três listas

def separador():
    print("-"*25)

separador()
print("Lista de números pares e ímpares")
separador()

valores = []
valores_par = []
valores_impares = []

print("Digite 20 pares a seguir")
for i in range(0, 20, 1):

    valores.append(int(input(f"Valor {i+ 1}: ")))

    if(valores[i] % 2 == 0):
        valores_par.append(valores[i])
    else:
        valores_impares.append(valores[i])

print(f"Valores digitados {valores}")
print(f"Valores pares {valores_par}")
print(f"Valores impares {valores_impares}")