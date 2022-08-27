# Antonio Claudio Teixeira Alves

# Leia um valor inteiro em sgundos, e imprima-o em horas, minutos e segundos.

def separador():
    print("-"*25)

separador()
print("Conversor de Segundos")
separador()

print("Quantidade de segundos: ", end="")
value = int(input())

seconds = value % 60
rest_minutes = value // 60
minutes = rest_minutes % 60
hour = rest_minutes // 60

print("{}:{}:{}".format(hour, minutes, seconds))