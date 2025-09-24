dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
dia_escolhido = ""
maior_votos = -1
for dia in dias_semana:
    votos = int(input(f"Quantidade de votos para {dia}: "))
    if votos > maior_votos:
        maior_votos = votos
        dia_escolhido = dia
print(f"O melhor dia para as lives é {dia_escolhido} com {maior_votos} votos.")