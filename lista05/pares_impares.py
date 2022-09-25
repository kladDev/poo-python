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

values = []
value_pair = []
value_odd = []

print("Digite 20 pares a seguir")
for i in range(0, 20, 1):

    values.append(int(input(f"Valor {i+ 1}: ")))

    if(valores[i] % 2 == 0):
        value_pair.append(value[i])
    else:
        value_odd.append(value[i])

print(f"Valores digitados {value}")
print(f"Valores pares {value_pair}")
print(f"Valores impares {value_odd}")
