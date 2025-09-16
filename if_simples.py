nome = input("Digite o nome do(a) funcionário(a): ")
salario = float(input("Digite o salário do(a) funcionário(a): "))

if salario < 0:
    salario = salario * -1
    print("Salário é negativo.")

print (f"O salário do(a) funcionário(a) {nome} é R$ {salario:.2f}")    

    