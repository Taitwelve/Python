porcentagens = {
    "Basic": 30,
    "Silver": 20,
    "Gold": 10,
    "Platinum": 5
}
tipo_assinatura = input("Digite o tipo de assinatura (Basic, Silver, Gold ou Platinum): ")
faturamento_anual = float(input("Digite o faturamento anual do cliente: "))
if tipo_assinatura in porcentagens:
    porcentagem = porcentagens[tipo_assinatura]
    bonus = (faturamento_anual * porcentagem) / 100
    print(f"O valor do bônus que o cliente deve pagar é de R${bonus:.2f}")
else:
    print("Tipo de assinatura inválido. Certifique-se de digitar Basic, Silver, Gold ou Platinum.")