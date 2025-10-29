itens = {}
while True:
    resp = input('Adicionar produtos? [S/N]').upper()
    if resp == 'N':
        break
    else:
        nome = input('Digite o nome do produto: ').lower()
        quantidade = int(input('Digite a quantidade: '))
        itens.update({nome:quantidade})
print(itens)