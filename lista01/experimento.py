# Antonio Claudio Teixeira Alves

# Faça um programa que leia o horário (hora, minuto, segundo) de inicio e a duração
# em segundo, de uma experiência biológica. O programa deve resultar com o novo
# horário (hora, minuto e segundo) do termino da mesma.

def separador():
    print("-"*25)


separador()
print("Duração do experimento")
separador()

print("Digite a seguir o horário do experimento")
print("Hora: ", end="")
hour = int(input())
print("Minutos: ", end="")
minutes = int(input())
print("Segundo: ", end="")
seconds = int(input())
print("")

print("Duração em segundos do experimento: ", end="")
s = int(input())

horary = (hour * 60 * 60) + (minutes * 60) + seconds
duration = horary + s


sec = duration % 60
rest_m = duration // 60
m = rest_m % 60
h = rest_m // 60

print(f"Duração {s}: {m}: {sec}")