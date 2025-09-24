quantidade_alimentos = int(input("Digite a quantidade de alimentos que você consumiu hoje: "))
total_calorias = 0
for alimento in range (1, quantidade_alimentos + 1, 1):
    calorias = int(input(f"Digite a quantidade de calorias do alimento {alimento}: "))
    total_calorias += calorias
print(f"O total de calorias consumidas hoje foi de {total_calorias} calorias.")
