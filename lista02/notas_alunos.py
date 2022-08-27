# Antonio Claudio Teixeira Alves

# Faça um programa que leia 2 notas de um aluno, verifique
# se as notas são válidas e exiba na tela a média destas notas.
# Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0
# e 10.0, onde caso a nota não possua um valor válido, este fato
# deve ser informado ao usuário e o programa termina.

def separador():
    print("-"*25)

separador()
print("\tSituação aluno")
separador()

note_one = float(input("Nota 01: "))
note_two = float(input("Nota 02: "))

if note_one <= 10 and note_one>= 0:
    if note_two <= 10 and note_two >= 0:
        print(f"Sua média é {(note_one+note_two)/2:.2f}")
else:
    print("Uma ou as duas notas são inválidas!")
