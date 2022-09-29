# Antonio Claudio Teixeira Alves
import math


# Faça uma função que receba a altura e
# o raio de um cilindro circular e retorne
# o volume do cilindro

def separador():
    print("-"*15)

def volume_do_cilindro(height, radius):
    return math.pi * pow(radius, 2) * height

separador()
print("VOLUME DO CILINDRO")
separador()

radius = float(input("Raio: "))
height = float(input("Altura: "))
volume = volume_do_cilindro(height, raio)

print(f"O volume do cilindro é {volume:.2f}")
