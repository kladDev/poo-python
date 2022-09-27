# Antonio Claudio Teixeira Alves

# Faça uma função que receba dois números
# e retorne qual deles é o maior

def separador():
    print("-"*15)

def biggest_value(first_value, second_value):
    if first_value > second_value:
        return first_value
    else second_value >= first_value:
        return second_value


separador()
print("MAIOR VALOR")
separador()

first_value = float(input("Valor 01: "))
second_value = float(input("Valor 02: "))
bigger = biggest_value(first_value, second_value)

print(f"Foram lidos {first_value:.2f} e {second_value:.2f}\nO maior valor é {bigger:.2f}")
