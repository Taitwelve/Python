from calculadora import *

op = -1 
while op != 0:
    print("Escolha a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Dividir")
    print("4 - Multiplicar")
    print("0 - Sair")
    op = int(input("Digite a opção desejada: "))
    
    if op in [1, 2, 3, 4]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if op == 1:
            resultado = somar(num1, num2)
            print(f"Resultado: {resultado}")
        elif op == 2:
            resultado = subtrair(num1, num2)
            print(f"Resultado: {resultado}")
        elif op == 3:
            resultado = dividir(num1, num2)
            print(f"Resultado: {resultado}")
        elif op == 4:
            resultado = multiplicar(num1, num2)
            print(f"Resultado: {resultado}")
    elif op == 0:
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")

        