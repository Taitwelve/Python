valor_compra = float(input("Informe o valor da compra realizada: "))
cupom = str(input("Digite o cupom de desconto: "))
if cupom.upper() == "NIVER10":
    print("DESCONTO APLICADO!")
    valor_final = float(valor_compra) * 0.9
else:
    valor_final = float(valor_compra)
    print("CUPOM INVÁLIDO")
print(f"O valor final da compra é R${valor_compra:.2f}")