voto1 = input("Informe qual o prêmio que você deseja ganhar: PLAYSTATION 5, XBOX SERIES X ou NINTENDO SWITCH: ")
voto2 = input("Informe qual o prêmio que você deseja ganhar: PLAYSTATION 5, XBOX SERIES X ou NINTENDO SWITCH: ")
voto3 = input("Informe qual o prêmio que você deseja ganhar: PLAYSTATION 5, XBOX SERIES X ou NINTENDO SWITCH: ")
voto4 = input("Informe qual o prêmio que você deseja ganhar: PLAYSTATION 5, XBOX SERIES X ou NINTENDO SWITCH: ")
voto5 = input("Informe qual o prêmio que você deseja ganhar: PLAYSTATION 5, XBOX SERIES X ou NINTENDO SWITCH: ")
playstation = 0
xbox = 0
nintendo = 0
if voto1.upper() == "PLAYSTATION 5":
    playstation += 1
elif voto1.upper() == "XBOX SERIES X":
    xbox += 1
elif voto1.upper() == "NINTENDO SWITCH":
    nintendo += 1
else:
    print("Voto inválido! Seu voto não será computado!")
if voto2.upper() == "PLAYSTATION 5":
    playstation += 1
elif voto2.upper() == "XBOX SERIES X":
    xbox += 1
elif voto2.upper() == "NINTENDO SWITCH":
    nintendo += 1
else:
    print("Voto inválido! Seu voto não será computado!")
if voto3.upper() == "PLAYSTATION 5":
    playstation += 1
elif voto3.upper() == "XBOX SERIES X":
    xbox += 1
elif voto3.upper() == "NINTENDO SWITCH":
    nintendo += 1
else:
    print("Voto inválido! Seu voto não será computado!")
if voto4.upper() == "PLAYSTATION 5":
    playstation += 1
elif voto4.upper() == "XBOX SERIES X":
    xbox += 1
elif voto4.upper() == "NINTENDO SWITCH":
    nintendo += 1
else:
    print("Voto inválido! Seu voto não será computado!")
if voto5.upper() == "PLAYSTATION 5":
    playstation += 1
elif voto5.upper() == "XBOX SERIES X":
    xbox += 1
elif voto5.upper() == "NINTENDO SWITCH":
    nintendo += 1
else:
    print("Voto inválido! Seu voto não será computado!")
print(f"Total de votos para PLAYSTATION 5: {playstation}")
print(f"Total de votos para XBOX SERIES X: {xbox}")
print(f"Total de votos para NINTENDO SWITCH: {nintendo}")

if playstation > xbox and playstation > nintendo:
    print("O console escolhido foi o PLAYSTATION 5!")
elif xbox > playstation and xbox > nintendo:
    print("O console escolhido foi o XBOX SERIES X!")
elif nintendo > playstation and nintendo > xbox:
    print("O console escolhido foi o NINTENDO SWITCH!")
else:
    print("Houve um empate entre os consoles! Favor entrar em contato com a direção!")
