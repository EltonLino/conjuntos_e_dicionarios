permissoes_principais = {'leitura', 'escrita', 'execução', 'compartilhamento'}
permissoes_solicitadas = set(input('Digite suas solicitações separadas por ,: ').split(', '))

if (permissoes_solicitadas.issubset(permissoes_principais)):
    print('As permissões solicitadas fazem parte das permissões principais.')
else:
    print('As permissões solicitadas não fazem parte das permissões principais.')