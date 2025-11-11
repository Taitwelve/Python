dicionario = {
    "Yoda": "Mestre Jedi", 
    "Vader": "Lord Sith", 
    "Leia": "Princesa",
    "Luke": "Cavaleiro Jedi",
    "Han Solo": "Piloto"
}
print (dicionario)
print (dicionario.values())
print (dicionario.keys())
print (dicionario["Yoda"])

for valor in dicionario.values():
    print (valor)

for chave in dicionario.keys():
    print (chave)    


print (dicionario.items())    

for chave, valor in dicionario.items():
    print (f"A chave é {chave} e o valor é {valor}")