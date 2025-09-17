email_aluno = input("Informe o e-mail do aluno: ")
nota_semestral = input("Informe a nota semestral do aluno: ")
nota_semestral = float(nota_semestral)
if nota_semestral > 8.5:
    print("ENVIANDO E-MAIL PARA {} COM APROVAÇÃO.".format(email_aluno))
else:
     print("ENVIANDO E-MAIL PARA {} PARA AGENDAMENTO DE PROVA DE RECUPERAÇÃO.".format(email_aluno))    