nota = int(input('Digite a sua nota: '))

if nota >= 7:
    print('Passou!')
elif nota < 5: # elif é o else if
    print('Não passou!')
else: 
    print('Recuperação!')