pontuacao = int(input("Informe a pontuação conquistada: "))

if pontuacao > 1000: 
    print("Você ganhou 3GB de bônus!")
else:
    if pontuacao > 500: 
        print("Você ganhou 1.5GB de bônus!")
    else:
        if pontuacao > 200: 
            print("Você ganhou 500MB de bônus!")
        else:
            print("Você não ganhou bônus!")        