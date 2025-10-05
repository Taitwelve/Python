#Função que calcula a velocidade média
def calcularVelocidadeMedia():
    #solicitar distância e tempo
    distancia = float(input("Digite a distância percorrida em quilometros: "))
    tempo = float(input("Digite o tempo da viagem em minutos: "))
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    print("A velocidade média é {} km/h".format(velocidade_media))

#aqui começa o programa principal
calcularVelocidadeMedia()
