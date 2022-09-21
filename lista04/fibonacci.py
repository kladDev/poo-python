# Antonio Claudio Teixeira Alves

# Leia um número positivo do usuário, então, calcule e imprima a
# sequência Fibonacci até o primeiro número superior ao número lido.
# Exemplo: se o usuário informou o número 30, a sequência a ser impressa será
# 0 1 1 2 3 5 8 13 21 34

def separador():
    print("-"*20)

separador()
print("Sequência de Fibonacci")
separador()

value = int(input("Digite até o número desejado: "))

previous = 0
next = 1
fibonacci = 0

for i in range(0, value, 0):
    print(fibonacci, end=" ")
    previous = next + previous
    next = fibonacci
    fibonacci = previous
