convidados = set()
while True:
    convidado = input('Digite o nome do convidado ou sair para encerrar: ')
    if convidado.lower() == 'sair':
        break
    else:
        convidados.add(convidado)

print(f"Convidados confirmados: {', '.join(convidados)}") 