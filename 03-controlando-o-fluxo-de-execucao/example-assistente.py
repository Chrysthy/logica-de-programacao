print('Olá, eu sou seu assistente virtual! O que você deseja fazer?')

comando = input('Digite o comando: ')

match comando:
    case "oi" | "olá":
        print('Olá, tudo bem?')
    
    case "tchau" | "adeus" | "até mais" | "sair":
        print('Tchau, até mais!')
    
    case "piada":
        print('Por que o livro de matemática se suicidou? Porque ele tinha muitos problemas.')
    
    case "clima":
        print('Hoje o dia está ensolarado com algumas nuvens ao longo do dia.')

    case _:
        print('Comando não reconhecido.')