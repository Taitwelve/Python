numero_usuario = int(input("Digite por favor um número inteiro: "))
anterior1 = 1
anterior2 = 0
for n_elementos in range(1, numero_usuario + 1, 1):
    atual = anterior1 + anterior2
    anterior2 = anterior1
    anterior1 = atual
    if numero_usuario == atual:
        print(f"O número {numero_usuario} pertence a sequência de Fibonacci. Parabéns!")
        break
    elif numero_usuario < atual:
        print(f"O número {numero_usuario} não pertence a sequência de Fibonacci. Fim!")
        break
