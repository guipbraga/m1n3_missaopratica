def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_reprovado(media, nota_minima=6.0):
    return media < nota_minima

def identificar_reprovados(dados_alunos, matriculas_reprovados):
    reprovados = []
    for aluno in dados_alunos:
        if aluno['matricula'] in matriculas_reprovados:
            media = calcular_media(aluno['notas'])
            reprovados.append(f"Aluno Reprovado: {aluno['nome']} – Matrícula: {aluno['matricula']} – Média Final: {media:.2f}")
    return reprovados