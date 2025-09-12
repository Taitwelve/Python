# valor1 = input("Digite o primeiro valor: ")
# valor2 = input("Digite o segundo valor: ")
# soma = int(valor1) + int(valor2)
# print("A soma é {}.".format(soma))
#------------------------------------------------------------
#Calculadora 
# valor1 = input("Por favor, digite o primeiro valor: ")
# valor2 = input("Por favor, digite o segundo valor: ")
# soma = float(valor1) + float(valor2)
# print("A soma entre os valores é {}".format(soma))
# subtracao = float(valor1) - float(valor2)
# print("A subtração entre os valores é {}".format(subtracao))
# divisao = float(valor1) / float(valor2)
# print("A divisão entre os valores é {}".format(divisao))
# multiplicacao = float(valor1) * float(valor2)
# print("A multiplicação entre os valores é {}".format(multiplicacao))
#------------------------------------------------------------
#Calculo de velocidade média
print("Esse programa calcula a velocidade média de um patinete")
distancia = input("Qual foi a distância em metros percorrida pelo patinete? ")
tempo = input("Quantos minutos o patinete demorou para percorrer essa distância? ")
velocidade_media = float(distancia) / float(tempo)
print("O patinete atingiu uma velocidade de {0:.2f} m/min".format(velocidade_media))
