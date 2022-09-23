# Antonio Claudio Teixeira Alves

# Faça um Programa que receba uma lista de 5
# números inteiros e mostre-os.


list = []
print("Adicione cinco valores a seguir")

for i in range(0, 5, 1):
    list.append(int(input(f"Valor 0{i+1}: ")))

print(list)
