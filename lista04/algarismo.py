# Antonio Claudio Teixeira Alves

# Escreva um algoritmo que leia um número inteiro entre 100 e 999
# e imprima na saída cada um dos algarismo que compõem o número

def separador():
    print("-"*20)

separador()
print("Decomposição de número")
separador()

value = int(input("Digite um valor (100 e 999): "))

if value >= 100 and value <= 999:
    print(f"Centena {value//100}")
    print(f"Dezena {value//10 - 10}")
    print(f"Unidade {value%10}")
