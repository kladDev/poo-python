# Antonio Claudio Teixeira Alves

# A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
# Sendo que da quantia total:
# O primeiro ganhador receberá 46%;
# O segundo receberá 32%;
# o terceiro receberá o restante
# Calcule e imprima a quantia ganha por cada um dos ganhadores

print("A recompensa do prêmio será dividido da seguinte forma")

first_winner = 780000 * 46 / 100
second_winner = 780000 * 32 / 100
third_winner = 780000 - first_winner - second_winner

print(f"O primeiro ganhará {first_winner:.2f}")
print(f"O sgundo {second_winner:.2f}")
print(f"O terceiro {third_winner:.2f}")
