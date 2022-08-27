# Antonio Claudio Teixeira Alves

# Escreva um program de ajuda para vendedores. A partir de um valor
# total lido, mostre:
# O total a pagar com desconto de 10%
# O valor de cada parcela, no parcelamento de 3x sem juros;
# A comissão do vendedors, no caso da venda ser a vista (5% sobre o valor
# com desconto)
# A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor total)

def separador():
    print("*"*25)

separador()
print("Valor da comissão total")
separador()

print("Digite o valor do(s) produto(s) a ser vendido(s)")
print("R$ ", end="")
value = float(input())
discount = value*0.1

print("")
print(f"A vista com 10% de desconto sairá R${value - discount:.2f}")
print(f"Parcelado em 3x sairá R${value/3:.2f} sem juros")
print("")

print(f"Já a sua comissão a vista será R${(value - discount) * 0.05}")
print(f"E parcelado seria R${value*0.05}")
