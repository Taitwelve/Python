resposta = "0"
while (resposta != "42"):
    resposta = input("Qual a resposta para a vida, o universo e tudo mais? ")
print("Parabéns, você acertou! Você é um verdadeiro(a) Geek!")


i = 0
while (i < 10):
    print(f"Mais uma repetição! Dessa vez o i vale: {i}")
    i += 1

numero = 1
while numero%2 == 1:
    numero = int(input("Digite um número par: "))
print(f"Obrigado por digitar o número {numero}, que é par!")    


n = int(input("Digite o número que você quer a tabuada: "))
i = 0
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1
print("Fim da tabuada! Espero ter ajudado! Bons estudos ☺️")