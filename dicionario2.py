dicionario = {}

dicionario["Taiane Nascimento"] = "Desenvolvedora"
nome_colaborador = input("Digite o nome do colaborador: ")
cargo_colaborador = input("Digite o cargo do colaborador: ")
dicionario[nome_colaborador] = cargo_colaborador

for nome, cargo in dicionario.items():
    print (f"O colaborador {nome} exerce o cargo de {cargo}")

