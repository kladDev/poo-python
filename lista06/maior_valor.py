# Antonio Claudio Teixeira Alves

# Faça uma função que receba dois números
# e retorne qual deles é o maior

def separador():
    print("-"*15)

def maior_valor(valor1, valor2):
    if valor1 > valor2:
        return valor1
    elif valor2 > valor1:
        return valor2
    else:
        return valor1

separador()
print("MAIOR VALOR")
separador()

valor1 = float(input("Valor 01: "))
valor2 = float(input("Valor 02: "))
maior = maior_valor(valor1, valor2)

print(f"Foram lidos {valor1:.2f} e {valor2:.2f}\nO maior valor é {maior:.2f}")