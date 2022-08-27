# Antonio Claudio Teixeira Alves

# Receba a altura do degrau de uma escada e a altura
# que o usuário deseja alcançar subindo a escada. Calcule
# e mostre quantos degraus o usuário deverá subir para atingir
# seu objetivo

def separador():
    print("-"*25)

separador()
print("Subindo escadas")
separador()

print("Digite a altura do degrau: ", end="")
stair = float(input())
print("Qual altura deseja atingir? ", end='')
height = float(input())
print("")

print(f"Você deverá subir {height/stair:.2f} escadas")