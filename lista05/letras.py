# Antonio Claudio Teixeira Alves

# Faça um Programa que leia lista de 10 caracteres, e
# diga quantas consoantes foram lidas. Imprima as consoantes.

def separador():
    print("-"*25)


character = []
consonants = []

separador()
print("Leitor de caracteres")
separador()

print("OBS:. Caso digitado mais de um caractere")
print("será considerado apenas o primeiro digitado")
print("")
print("Digite 10 caracteres abaixo")

for i in range(0, 10, 1):
    letter = input(f"{i+ 1}º caractere: ")[0]
    character.append(letra.lower())

print(character)

for i in "bcdfghjklmnpqrstvwxyz":
    for j in range(10):
        if i == character[j]:
            consonants.append(caracteres[j])

print(f"Foram lidas {len(consonants)} consoantes")
print(consonants)
