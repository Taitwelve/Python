categorias = ("padawan", "jedi", "cavaleiro jedi", "mestre jedi")
# As tuplas são imutáveis, ou seja, não podem ser alteradas após a criação.
print(categorias)
print(categorias[1])

teste1, teste2, teste3, teste4 = categorias
print(teste1)
print(teste2)
print(teste3)
print(teste4)   
# Desempacotamento de tuplas. A tuupla entende que cada variável receberá o valor correspondente à sua posição na tupla.


for categoria in categorias:
    print(categoria)
# Iterando sobre os elementos da tupla com um loop for.
