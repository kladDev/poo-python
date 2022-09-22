# Antonio Claudio Teixeira Alves

# Faça um programa que leia um número inteiro N e depois
# imprima os N primeiros números naturais ímpares

def separador():
    print("-"*30)

separador()
print("Primeiros números naturais ímpares")
separador()
value = int(input("Digite o limite: "))

for i in range(1, value, 1):
    if i % 2 != 0 and value >= 0:
        print(i, end=" ")
