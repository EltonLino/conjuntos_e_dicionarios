participantes = { 
    "Mariana": 25, 
    "Carlos": 32, 
    "Beatriz": 28, 
    "Rafael": 35 
} 

opcao = (input('''
Digite a opção desejada:
1 - Nome dos participantes
2 - Idade dos participantes
3 - Todas as informações
'''))

match opcao:
    case '1':
        print('Nome dos participantes: ' + ', '.join(participantes))
    case '2':
        print('Idade dos participantes: ' + ', '.join(map(str,participantes.values())))
    case '3':
        for i, j in participantes.items():
            print(f'- {i}: {j}')
    case _:
        print('Opção Inválida')