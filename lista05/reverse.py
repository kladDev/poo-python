# Antonio Claudio Teixeira Alves

# Faça um Programa que receba uma lista de 10
# números reais e mostre-os na ordem inversa

def separador():
    print("-"*30)

list = []

separador()
print("Mostrar lista em ordem reversa")
separador()
print("Digite 10 números abaixo")

for i in range(0, 10, 1):
    list.append(float(input(f"Valor {i + 1}: ")))

list.reverse()
print(list)
