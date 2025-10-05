lista = ["Guitarra", "Baixo", "Bateria", "Teclado", "Violão"]
print(lista)
#Adicionando um item ao final da lista
lista.append("Flauta")
print(lista)
#Pedir ao usuário para adicionar um item ao final da lista
lista.append(input("Digite o nome de um instrumento musical: "))
print(lista)
#Adicionando um item em uma posição específica da lista
lista.insert(2, "Saxofone")
print(lista)
#Removendo o último item da lista
lista.pop()
print(lista)
#Removendo um item em uma posição específica da lista
lista.pop(2)
print(lista)
#Removendo um item pelo nome
lista.remove("Baixo")
print(lista)