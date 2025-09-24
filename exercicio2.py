valor_bruto = float(input("Digite o valor bruto da viagem: "))
categoria = input("Digite a categoria da viagem: ECONÔMICA, EXECUTIVA ou PRIMEIRA CLASSE: ")
quantidade_viajantes = int(input("Digite a quantidade de viajantes: "))
valor_desconto = 0

if categoria.upper() == "ECONÔMICA":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.03
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.04
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.05
elif categoria.upper() == "EXECUTIVA":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.05
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.07
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.08
elif categoria.upper() == "PRIMEIRA CLASSE":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.1
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.15
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.2        
else:
    print("Categoria inválida! Nenhum desconto será aplicado.")

valor_liquido = valor_bruto - valor_desconto
media_por_pessoa = valor_liquido / quantidade_viajantes    

print(f"O valor da viagem é R$ {valor_bruto:.2f}. Após aplicado o desconto de R$ {valor_desconto:.2f}, passará a custar R$ {valor_liquido:.2f}. Sendo R$ {media_por_pessoa:.2f} por pessoa.")
