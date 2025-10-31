participantes = {
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"},
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"}
}

remover = input('Nome do participante removido: ')

encontrado = False
for workshop, nomes in participantes.items():
    if remover in nomes:          
        nomes.discard(remover)    
        encontrado = True
        break

if not encontrado:
    print('Participante não cadastrado')

print(participantes)