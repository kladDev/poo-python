# Antonio Claudio Teixeira Alves

# Faça um Programa que leia lista de 10 caracteres, e
# diga quantas consoantes foram lidas. Imprima as consoantes.

def separador():
    print("-"*25)


caracteres = []
caracteres_consoantes = []

separador()
print("Leitor de caracteres")
separador()

print("OBS:. Caso digitado mais de um caractere")
print("será considerado apenas o primeiro digitado")
print("")
print("Digite 10 caracteres abaixo")

for i in range(0, 10, 1):
    letra = input(f"{i+ 1}º caractere: ")[0]
    caracteres.append(letra.lower())

print(caracteres)

for i in "bcdfghjklmnpqrstvwxyz":
    for j in range(0, 10, 1):
        if i == caracteres[j]:
            caracteres_consoantes.append(caracteres[j])

print(f"Foram lidas {len(caracteres_consoantes)} consoantes")
print(caracteres_consoantes)

