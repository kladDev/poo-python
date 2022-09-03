# Antonio Claudio Teixeira Alves

# Faça um Programa que receba uma lista de 10
# números reais e mostre-os na ordem inversa

def separador():
    print("-"*30)

lista = []

separador()
print("Mostrar lista em ordem reversa")
separador()
print("Digite 10 números abaixo")

for i in range(0, 10, 1):
    lista.append(float(input(f"Valor {i + 1}: ")))

lista.reverse()
print(lista)