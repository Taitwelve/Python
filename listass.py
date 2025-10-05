def somar ():
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número para somar ao primeiro: "))
    soma = a + b
    print("A soma entre {} e {} é igual a {}".format(a, b, soma))
somar()

def subtrair ():
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número para subtrair do primeiro: "))
    subtracao = a - b
    print("A subtração entre {} e {} é igual a {}".format(a, b, subtracao))
subtrair()

def multiplicar ():
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número para multiplicar pelo primeiro: "))
    multiplicacao = a * b
    print("A multiplicação entre {} e {} é igual a {}".format(a, b, multiplicacao))
multiplicar()

def dividir ():
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número para dividir o primeiro: "))
    divisao = a / b
    print("A divisão entre {} e {} é igual a {}".format(a, b, divisao))
dividir()   

# Refactored version of the sum function
def soma (a, b):
    somando = a + b
    print("A soma entre {} e {} é igual a {}".format(a, b, somando))

valor1 = float(input("Digite um número: "))
valor2 = float(input("Digite outro número para somar ao primeiro: "))
soma(valor1, valor2)    
soma (5, 10)