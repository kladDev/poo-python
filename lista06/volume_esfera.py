# Antonio Claudio Teixeira Alves
import math


# Faça uma função e um programa de
# teste para o cálculo do volume de
# uma esfera. Sendo que o raio é
# passado por parâmetro

def separador():
    print("-"*20)

def volume_da_esfera(radius):
    return math.pi * pow(radius, 3) * 4/3

separador()
print("Volume da esfera")
separador()

radius = float(input("Digite o RAIO da esfera: "))
volume = volume_da_esfera(radius)
print(f"O volume da esfera é {volume:.2f}")
