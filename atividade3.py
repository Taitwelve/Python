notas_pares = []
notas_impares = []
for aluno_numero in range(1, 51):
    nota = float(input(
        f"VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS {'ÍMPARES' if aluno_numero % 2 != 0 else 'PARES'}. POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {aluno_numero}: "))

    if aluno_numero % 2 != 0:
        notas_impares.append(nota)
    else:
        notas_pares.append(nota)
media_pares = sum(notas_pares) / len(notas_pares)
media_impares = sum(notas_impares) / len(notas_impares)
print(f"A média das notas dos alunos PARES é: {media_pares:.2f}")
print(f"A média das notas dos alunos ÍMPARES é: {media_impares:.2f}")
if media_pares > media_impares:
    print("A metade dos alunos PARES teve a maior nota.")
elif media_impares > media_pares:
    print("A metade dos alunos ÍMPARES teve a maior nota.")
else:
    print("As duas metades tiveram a mesma média de notas.")
