valor_compra = float(input("Digite o valor da sua compra: "))
forma_pagamento = int(input("1 - Dinheiro | 2 - Cartão : "))

if valor_compra > 100 or forma_pagamento == 1 :
    valor_compra = valor_compra * 0.9
    print("Você tem direito a 10% de desconto!")

print(f"O valor a pagar é R${valor_compra}")    