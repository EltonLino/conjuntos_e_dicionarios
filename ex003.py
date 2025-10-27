lista_laura = set(input('Lista Laura: ').strip().split(', '))
lista_ana = set(input('Lista Ana: ').strip().split(', '))

comuns = lista_laura & lista_ana
laura = lista_laura - lista_ana
ana = lista_ana - lista_laura

print(f'Itens em ambas as listas: {', '.join(comuns)}')
print(f'Itens exclusivos de Laura: {', '.join(laura)}')
print(f'Itens exclusivos de Ana: {', '.join(ana)}')