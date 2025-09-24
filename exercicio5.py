quantidade_transacoes = int(input("Digite a quantidade de transações que você realizou hoje: "))
total_transacoes = 0
for n_transacao in range(1, quantidade_transacoes + 1, 1):
    valor_transacao = float(input(f"Digite o valor da transação {n_transacao}: R$ "))
    total_transacoes = total_transacoes + valor_transacao
media = total_transacoes / quantidade_transacoes 
print(f"O total das transações realizadas hoje foi de R$ {total_transacoes:.2f} e a média das transações foi de R$ {media:.2f}.")   

    