# Antonio Claudio Teixeira Alves

#  Leia o salário de um trabalhador e o valor da prestação
#  de um empréstimo. Se a prestação for maior que 20% do salário
#  imprima: Empréstimo não concedido, caso contrário imprima:
#  Empréstimo concedido

def separador():
    print("-"*25)

separador()
print("Empréstimo certo")
separador()

salary = float(input("Digite seu salário atual R$ "))
print("Gostaria de dividir o empréstimo em quantas parcelas")
p = float(input("Quantidade de parcela: R$ "))

if p > (salary * 0.2):
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")
