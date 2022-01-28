def notas(*notas, sit=False):
    """
    Notas do Aluno
    :param notas: recebe uma lista com as notas dos alunos
    :param sit: caso parâmetro recebido seja True o retorno inclui a situação final do aluno no semestre
    :return: dicionario com Total de notas digitadas, maior nota, menor nota, media e situacao do aluno no semestre.
    """
    dicNotas = dict()
    dicNotas['Total'] = len(notas)
    dicNotas['Maior'] = max(notas)
    dicNotas['Menor'] = min(notas)
    dicNotas['Media'] = sum(notas) / len(notas)

    if sit:
        if dicNotas['Media'] > 7:
            dicNotas['Situação'] = "Boa"
        elif dicNotas['Media'] >= 5:
            dicNotas['Situação'] = "Razoável"
        else:
            dicNotas['Situação'] = "Ruim"

    return dicNotas

#Programa principal
resp = notas(8.0, 4.5, 3.2, 5.0, 10.0, sit=True)
help(notas)
print(resp)




