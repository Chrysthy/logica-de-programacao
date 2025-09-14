# snake_case - funções e variáveis em Python
# camelCase - usado em JS e Java, mas não em Python
# PascalCase - recomendado para nomes de classes em Python
# kebab-case - não pode usar em variáveis
# SCREAMING_SNAKE_CASE - usado pra constantes em Python

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

# Sempre utilize nomes descritivos para funções e variáveis
# verbos no infinitivo para funções
# snake_case em Python
# separar resoponsabilidades das funções