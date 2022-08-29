# Antonio Claudio Teixeira Alves

# Escreva um algoritmo que leia certa quantidade de números e imprima
# o maior deles e quantas vezes o maior valor número foi lido. A quan-
# tidade de números a serem lidos deve ser fornecida pelo usuário.

def separador():
    print("-"*20)

separador()
print("Maior Número")
separador()

quantidade_de_numeros = int(input("Deseja digitar quantos números? "))
vezes_lida_maior = 0


for i in range(0, quantidade_de_numeros, 1):
    valores = int(input(f"Digite o {i+1}º valor: "))

    if i == 0:
        maior_valor = valores

    if valores > maior_valor:
        maior_valor = valores
        vezes_lida_maior += 1

print(f"O maior valor é {maior_valor} e foi lido {vezes_lida_maior}")