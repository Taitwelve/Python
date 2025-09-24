print("Verificador de batimentos cardíacos por minuto")
idade = int(input("Digite sua idade: "))
bpm = int(input("Digite o número dos seus batimentos por minuto: "))
if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Sua frequência cardíaca está normal!")
    else:
        print("Sua frequência cardíaca está fora do normal!")
elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Sua frequência cardíaca está normal!")
    else:
        print("Sua frequência cardíaca está fora do normal!")
elif idade >= 18 and idade <= 65:
    if bpm >= 70 and bpm <= 80:
        print("Sua frequência cardíaca está normal!")
    else:
        print("Sua frequência cardíaca está fora do normal!")
elif idade > 65:
    if bpm >= 50 and bpm <= 60:
        print("Sua frequência cardíaca está normal!")
    else:
        print("Sua frequência cardíaca está fora do normal!")
else:
    print("Idade inválida!")