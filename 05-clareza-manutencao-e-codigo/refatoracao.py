# Código sem refatoração
# nota1 = 7
# nota2 = 6
# media = (nota1 + nota2) / 2
# if media >= 6:
#     print("Aprovado")
# else:
#     print("Reprovado")

# nota3 = 8
# nota4 = 9
# media2 = (nota3 - nota4) / 2
# if media2 > 6:
#     print("Aprovado")
# else:
#     print("Reprovado")




def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


nota1 = 5
nota2 = 3
media = calcular_media(nota1, nota2)

print(f'{verificar_aprovacao(media)} com média {media}')

nota3 = 10
nota4 = 9
media2 = calcular_media(nota3, nota4)

print(f'{verificar_aprovacao(media2)} com média {media2}')
