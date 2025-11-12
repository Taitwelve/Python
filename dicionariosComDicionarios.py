contatos = {
    'João': {
        'telefone': '1234-5678',
        'email': 'joao@example.com'
    },
    'Maria': {
        'telefone': '9876-5432',
        'email': 'maria@example.com'
    }
}
print(contatos.keys())
print(contatos.values())
print(contatos.items())

for nome, info in contatos.items():
    print (f"O contato {nome}")
    for chave, valor in info.items():
        print (f"Pode ser contatado pelo {chave} através do {valor}")
print("\n\n")
