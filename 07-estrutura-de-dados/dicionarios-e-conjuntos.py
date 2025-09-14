# Dicionários e Conjuntos

estudantes = {
    1: {'nome': 'Chrys', 'idade': 33, 'curso': 'Sistemas de Informação'},
    2: {'nome': 'Noob', 'idade': 15, 'curso': 'Engenharia'},
    3: {'nome': 'Leon', 'idade': 4, 'curso': 'Sistemas de Informação'}
}

cursos = {"Sistemas de Informação", "Engenharia", "Medicina"}

estudantes_cursos = {
    "Sistemas de Informação": {1, 3},
    "Engenharia": {2}
}


def adiciona_estudante(matricula, nome, idade, curso):

    pessoa = {'nome': nome, 'idade': idade, 'curso': curso}
    estudantes[matricula] = pessoa

    if curso not in estudantes_cursos:
        estudantes_cursos[curso] = set()
    estudantes_cursos[curso].add(matricula)


# print(estudantes_cursos)
# adiciona_estudante(5, 'Collin', 4, 'Sistemas de Informação')
# print(estudantes_cursos)
# adiciona_estudante(6, 'Pisquilo', 5, 'Física')
# print(estudantes_cursos)

print(f'Todas as pessoas matriculadas em algum curso: {estudantes_cursos["Engenharia"]} | {estudantes_cursos["Sistemas de Informação"]}')
