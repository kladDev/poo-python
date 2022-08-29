# Antonio Claudio Teixeira Alves

# Escreva um algoritmo que leia um número inteiro entre 100 e 999
# e imprima na saída cada um dos algarismo que compõem o número

def separador():
    print("-"*20)

separador()
print("Decomposição de número")
separador()

valor = int(input("Digite um valor (100 e 999): "))

if valor >= 100 and valor <= 999:
    print(f"Centena {valor//100}")
    print(f"Dezena {valor//10 - 10}")
    print(f"Unidade {valor%10}")
