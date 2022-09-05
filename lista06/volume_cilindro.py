# Antonio Claudio Teixeira Alves
import math


# Faça uma função que receba a altura e
# o raio de um cilindro circular e retorne
# o volume do cilindro

def separador():
    print("-"*15)

def volume_do_cilindro(altura, raio):
    return math.pi * pow(raio, 2) * altura

separador()
print("VOLUME DO CILINDRO")
separador()

raio = float(input("Raio: "))
altura = float(input("Altura: "))
volume = volume_do_cilindro(altura, raio)

print(f"O volume do cilindro é {volume:.2f}")