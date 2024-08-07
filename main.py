from operacoes import calcular_media, verificar_reprovado, identificar_reprovados

dados_alunos = [
    {'nome': 'Maria', 'matricula': '26', 'notas': [8.0, 7.0, 5.0, 9.0]},
    {'nome': 'Ana', 'matricula': '101', 'notas': [9.0, 9.0, 8.0, 9.0]},
    {'nome': 'João', 'matricula': '13', 'notas': [6.0, 5.0, 5.0, 5.0]},
    {'nome': 'Ágatha', 'matricula': '37', 'notas': [8.0, 6.0, 7.5, 9.0]},
    {'nome': 'Joaquim', 'matricula': '72', 'notas': [6.0, 5.5, 5.0, 7.0]},
    {'nome': 'Félix', 'matricula': '5', 'notas': [5.0, 10.0, 8.0, 8.0]}
]

matriculas_reprovados = []

for aluno in dados_alunos:
    media = calcular_media(aluno['notas'])
    if verificar_reprovado(media):
        matriculas_reprovados.append(aluno['matricula'])

alunos_reprovados = identificar_reprovados(dados_alunos, matriculas_reprovados)

print()
for aluno in alunos_reprovados:
    print(aluno)