dicionario = {
    "Ronaldinho Gaúcho": "Atacante", 
    "Ronaldo Fenômeno": "Atacante", 
    "Kaká": "Meia",
    "Cafu": "Lateral Direito",
    "Roberto Carlos": "Lateral Esquerdo"
}

for chave, valor in dicionario.items():
    print (f"O jogador {chave} atua como {valor}")
print("")

dicionario.pop("Kaká")


for chave, valor in dicionario.items():
    print (f"O jogador {chave} atua como {valor}")
print("")

dicionario.popitem()

for chave, valor in dicionario.items():
    print (f"O jogador {chave} atua como {valor}")