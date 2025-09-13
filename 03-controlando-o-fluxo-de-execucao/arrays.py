notas = [9, 9.5, 10, 8.5]

print(notas)

media = 0 
for nota in notas:
    print(nota)
    media += nota

media /= 4
print(f'A média é {media}')