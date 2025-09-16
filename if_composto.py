nome = input("Digite o nome do(a) aluno(a): ")
idade = int(input("Digite a idade do(a) aluno(a): "))

if idade < 18:
    print(f"{nome} é menor de idade. Consultar responsável.")
else:
    print(f"{nome} é maior de idade. Não é necessário consultar responsável.")