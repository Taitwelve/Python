minutos = int(input("Digite o número de minutos: "))
fatorial = 1
for i in range(1, minutos + 1):
    fatorial *= i
senha = "LIBERDADE" + str(fatorial)
print(f"A senha necessária para desbloqueio é: {senha}")
